from django.db import models
from django.utils import timezone

# Create your models here.

class Gif(models.Model):
    title = models.CharField(max_length = 100)
    url = models.URLField()
    uploader_name = models.CharField(max_length = 100)
    likes = models.PositiveIntegerField(default = 0)
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length = 100)
    gifs = models.ManyToManyField(Gif,related_name='categories', blank=True)

    def __str__(self):
        return f"{self.name} {self.id}"

