from django.shortcuts import render
from .models import Post


def home(request):
    return render(request, "home.html")


def posts_index(request):
    return render(request, "posts/index.html", {"posts": posts})


class Post:  # Note that parens are optional if not inheriting from another class
  def __init__(self, caption):
    self.caption = caption


posts = [
  Post('Ello mate very long but sweet caption. '),
]