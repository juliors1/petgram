from django.shortcuts import render
from .models import Post


def home(request):
    return render(request, "home.html")


def posts_index(request):
    posts = Post.objects.all()
    return render(request, "posts/index.html", {"posts": posts})


def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "posts/detail.html", {"post": post})
