# import form class from django
from django import forms
from .models import Gif,Category

# create a ModelForm
class GifForm(forms.ModelForm):
    demo_choices = [ (category.id,category.name) for category in Category.objects.all()]
    # categories = forms.MultipleChoiceField(choices = demo_choices)
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        # widget=forms.CheckboxSelectMultiple
    )
    
    # categories = forms.MultipleChoiceField(queryset =  Category.objects.all())
	# specify the name of model to use
    class Meta:
        model = Gif
        fields = ['title','url','uploader_name','categories']

class CategoryForm(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = Category
		fields = ['name']

# class LikeForm(forms.ModelForm):
# 	# specify the name of model to use
# 	class Meta:
# 		model = Gif
# 		fields = ['likes']
#         widgets = {'likes': forms.HiddenInput()}