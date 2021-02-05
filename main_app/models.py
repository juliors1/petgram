from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    caption = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"post_id": self.id})


