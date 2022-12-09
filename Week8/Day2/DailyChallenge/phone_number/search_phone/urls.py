from django.urls import path
from . import views

urlpatterns = [
    path('phonenumber/<str:phone>/',views.phonenumber,name='phonenumber' ),
    path('name/<str:name>/',views.name,name='name'),
    path('search/',views.person,name='person'),
]
