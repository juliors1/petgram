from django.db import models
from django.urls import reverse


class Post(models.Model):
    name = models.CharField(max_length=25)
    caption = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"post_id": self.id})
