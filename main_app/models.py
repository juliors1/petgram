from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.TextField(default='https://mspgh.unimelb.edu.au/__data/assets/image/0011/3576098/Placeholder.jpg')
    bio = models.TextField(max_length=250, blank=True)


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

    def __str__(self):
        return f"Photo for post_id: {self.post_id} @{self.url}"

# class Comment(models.Model):
#     post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
#     body = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return "%s - %s" % (self.name)