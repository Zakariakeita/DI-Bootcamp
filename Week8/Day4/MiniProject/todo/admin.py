from django.contrib import admin
from todo.models import Category,Todo

# Register your models here.

admin.site.register(Todo)
admin.site.register(Category)