from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("posts/", views.posts_index, name="index"),



]