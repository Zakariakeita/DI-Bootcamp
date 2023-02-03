from datetime import datetime
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime

class Categorie(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name=("Categorie")
        verbose_name_plural=("Categorie")
        
    def __str__(self):
        return   f'{self.name}'


class Gif(models.Model):
    title = models.CharField(max_length=100)
    URL = models.URLField()
    uploader_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default = datetime.today())
    categorie = models.ManyToManyField(Categorie, related_name='categories', blank=True)
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)
    def __str__(self):
           return f'{self.title}'
