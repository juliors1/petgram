from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    caption = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)




