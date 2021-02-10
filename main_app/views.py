from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post, Photo, Profile, User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3


S3_BASE_URL = "https://s3.us-east-1.amazonaws.com/"
BUCKET = "petgram"



@login_required
def posts_index(request):
    posts = Post.objects.all()
    return render(request, "posts/index.html", {"posts": posts})


@login_required
def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    total_likes = post.total_likes()
    liked = False
    if post.likes.filter(id=request.user.id).exists():
      liked = True
    return render(
        request, "posts/detail.html", {"post": post, "total_likes": total_likes, 'liked': liked})

@login_required
def users_index(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, "accounts/index.html", {"users": users})


@login_required
def users_detail(request, user_id):
    current_user = User.objects.get(id=user_id)
    posts_you_dont_have = Post.objects.exclude(users__exact=request.user)
    return render(
        request,
        "accounts/detail.html",
        {"current_user": current_user, "posts_you_dont_have": posts_you_dont_have},
    )


@login_required
def profile(request):
    user = User.objects.get(id=request.user.id)
    return render(request, "main_app/accounts/profile.html", {"user": user})


class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ["photo", "bio"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = "/accounts/profile/"


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ["photo", "bio"]
    success_url = "/accounts/profile/"


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["caption"]

    def form_valid(self, form):
        form.instance.user = self.request.user  # form.instance are the posts
        return super().form_valid(form)


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))

    if  post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)

    else:
        post.likes.add(request.user)
       

    return HttpResponseRedirect(reverse("detail", args=[str(pk)]))


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["caption"]


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/posts/"


def home(request):
    return render(request, "home.html")


def signup(request):
    error_message = ""
    if request.method == "POST":
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect("index")
        else:
            error_message = "Invalid sign up - try again"
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)


@login_required
def add_photo(request, post_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get("photo-file", None)
    if photo_file:
        s3 = boto3.client("s3")
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind(".") :]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to post_id or post (if you have a post object)
            photo = Photo(url=url, post_id=post_id)
            photo.save()
        except:
            print("An error occurred uploading file to S3")
    return redirect("detail", post_id=post_id)
