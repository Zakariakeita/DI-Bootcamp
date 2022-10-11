from django.urls import path
from . import views

urlpatterns = [
    path('people/', views.people1, name='people1'),
    path('people/<int:id>/', views.people2, name='people2'),
]