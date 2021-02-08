from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required



class PostCreate(CreateView):
    model = Post
    fields = ["name","caption"]

    def form_valid(self, form):
        form.instance.user = self.request.user # form.instance are the posts
        return super().form_valid(form)


class PostUpdate(UpdateView):
    model = Post
    fields = [ "name","caption"]

class PostDelete(DeleteView):
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