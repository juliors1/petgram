from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.CharField(max_length=200, blank=True)
    bio = models.TextField(max_length=250, blank=True)


    def __str__(self):
        return f"Profile for user: {self.user.first_name} at user_id {self.user_id}, profile object {self.id}."

class Post(models.Model):
    name = models.CharField(max_length=25)
    caption = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="post_likes")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"post_id": self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)