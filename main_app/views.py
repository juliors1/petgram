from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
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


def posts_index(request):
    posts = Post.objects.all()
    return render(request, "posts/index.html", {"posts": posts})


def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "posts/detail.html", {"post": post})

