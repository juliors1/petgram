from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("posts/", views.posts_index, name="index"),
    path("posts/<int:post_id>/", views.posts_detail, name="detail"),
    path("posts/create/", views.PostCreate.as_view(), name="posts_create"),
    path("posts/<int:pk>/update/", views.PostUpdate.as_view(), name="post_update"),
    path("posts/<int:pk>/delete/", views.PostDelete.as_view(), name="post_delete"),
    path("posts/<int:post_id>/add_photo", views.add_photo, name="add_photo"),
    path("like/<int:pk>", views.LikeView, name="like_post"),
    path("accounts/signup/", views.signup, name="signup"),
    path("accounts/profile/", views.profile, name="profile"),
    path("accounts/addprofile/", views.ProfileCreate.as_view(), name="profiles_create"),
    # path("accounts/<int:pk>/update", views.ProfileUpdate.as_view(), name="profiles_update"),


]