from django.shortcuts import render
from .models import Post

def home(request):
    return render(request, "home.html")

def posts_index(request):
    posts = Post.objects.all()
    return render(request, "posts/index.html", { "posts" : posts})

