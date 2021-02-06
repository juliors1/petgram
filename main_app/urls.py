from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("posts/", views.posts_index, name="index"),
    path("posts/<int:post_id>/", views.posts_detail, name="detail"),
    path("posts/create/", views.PostCreate.as_view(), name="posts_create"),
    path("posts/<int:pk>/update/", views.PostUpdate.as_view(), name="post_update"),
    path("posts/<int:pk>/delete/", views.PostDelete.as_view(), name="post_delete"),




]