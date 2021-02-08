from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post, Photo
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3


S3_BASE_URL = "https://s3.us-east-1.amazonaws.com/"
BUCKET = "petgram"
class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    fields = ["name","caption"]

    def form_valid(self, form):
        form.instance.user = self.request.user # form.instance are the posts
        return super().form_valid(form)

def LikeView(request, pk):
    post = get_object_or_404(Post, id= request.POST.get("post_id"))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse("detail", args=[str(pk)]))

class PostUpdate(LoginRequiredMixin,UpdateView):
    model = Post
    fields = [ "name","caption"]

class PostDelete(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = "/posts/"

def home(request):
    return render(request, "home.html")

@login_required
def posts_index(request):
    posts = Post.objects.all()
    return render(request, "posts/index.html", {"posts": posts})

@login_required
def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "posts/detail.html", {"post": post})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def add_photo(request, post_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to post_id or post (if you have a post object)
            photo = Photo(url=url, post_id=post_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', post_id=post_id)