from django.db import models

# Create your models here.
class Famille(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=True)
    legs = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    speed = models.IntegerField()
    family = models.ForeignKey(Famille , on_delete=models.CASCADE)


   