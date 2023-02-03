from django.contrib import admin
from .models import Gif
from .models import Categorie
# Register your models here.
class AdminGifs(admin.ModelAdmin):
    list_display=('id','title','URL','uploader_name','created_at')
admin.site.register(Gif,AdminGifs)



class AdminCategory(admin.ModelAdmin):
    list_display=('id','name')
admin.site.register(Categorie,AdminCategory)    
