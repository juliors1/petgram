from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("post/create/",views.PostCreate.as_views(), name="post_create")


]