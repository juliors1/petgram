from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    name = models.CharField(max_length=25)
    caption = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"post_id": self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)