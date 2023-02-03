from django import forms
from .models import Gif
from .models import Categorie


#create form



class GifForm(forms.ModelForm):
    class Meta:
        model = Gif
        fields = ['uploader_name', 'title','URL','categorie']


class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['name']
        
