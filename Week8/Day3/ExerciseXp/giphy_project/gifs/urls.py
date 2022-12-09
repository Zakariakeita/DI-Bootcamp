from django.urls import path #path function
from . import views

urlpatterns = [
    path('', views.homepage, name='gifs.homepage'),
    path('add_category/', views.add_new_category, name='gifs.new_category'),
    path('add_gif/', views.add_new_gif, name='gifs.new_gifs'),
    path('category/<int:id>/', views.category, name='gifs.category'),
    path('gif/<int:id>/', views.gif, name='gifs.gif'),
    path('categories/', views.categories, name='gifs.categories'),
    path('populate/', views.populate, name='gifs.populate'),
    path('like/<int:like_id>/', views.like, name='gifs.like'),
    path('dislike/<int:dislike_id>/', views.dislike, name='gifs.dislike'),
    path('total of like/', views.totallike, name='gifs.totallike'),
]

