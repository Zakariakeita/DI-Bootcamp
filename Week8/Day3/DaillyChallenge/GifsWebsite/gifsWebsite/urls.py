"""gifs_projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from gifs.views import GifsCategorie, Homepage,Add,Categories,CategoriesGifs,Gif_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Homepage,name='home'),
    path('gif/',Add,name='add'),
    path('categories/',Categories,name='categories'),
    path('categorie/<int:id>/',GifsCategorie,name='categorie'),
    # path('view_categories',ViewCategories,name='view_categories'),
    path('categories_gifs/<int:id>',CategoriesGifs,name='categories_gifs'),
    path('gif_detail/<int:id>',Gif_detail,name='gif_detail'),
]
