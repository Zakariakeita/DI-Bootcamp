from django.db import models
from django.utils import timezone
from datetime import datetime


# Create your models here.

class Category(models.Model):
    name  = models.CharField(max_length = 30)
    image = models.ImageField(upload_to = 'upload/')

    # def __str__(self):
    #     return self.name

    def elem(self):
        return self

class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.username

class Todo(models.Model):
    title = models.CharField(max_length = 40)
    details = models.TextField()
    date_creation = models.DateTimeField(default = timezone.now)
    date_completion = models.DateTimeField(default=timezone.now)
    deadline_date  = models.DateTimeField()
    has_been_done = models.BooleanField(default = False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name = 'category')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name = 'users')

    def __str__(self):
        return self.title

    def deadline(self):
        delta = timezone.make_naive(self.deadline_date) - datetime.now()
        if delta.days<0:
            return "Deadline date already passed"
        if delta.days < 2:
            return "Deadline date is close"
        if delta.days >= 7:
            return "Deadline date is far"
        return ""

    def congratule(self):
        delta = timezone.make_naive(self.deadline_date) - timezone.make_naive(self.date_completion)
        if delta.days > 0:
            return True
        return False