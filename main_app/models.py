from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=25)
    caption = models.CharField(max_length=500)


    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("detail", kwargs={"post_id": self.id})
