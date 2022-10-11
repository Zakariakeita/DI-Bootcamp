from django.urls import path
from . import views


urlpatterns = [
    path('family/<int:id>/', views.family, name='family'),
    path('animals/<int:id>/', views.animals, name='animals'),
    path('animals/', views.animalslist, name='animalslist'),
]

