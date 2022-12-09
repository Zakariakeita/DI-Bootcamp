from .models import Todo,Category,User
from django import forms
from django.core.exceptions import ValidationError

categories = [(cat.id,cat.name) for cat in Category.objects.all()]

class AddTodoForm(forms.Form):
    title = forms.CharField()
    category = forms.ChoiceField(choices = categories)
    details = forms.CharField(widget = forms.Textarea)
    deadline_date = forms.DateTimeField(widget = forms.SelectDateWidget)
    # class Meta:
    #     model = Todo
    #     fields = ['title','details','deadline_date','category']



class signupForm(forms.Form,forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirmation = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','password']

    def clean(self):
        cleaned_data = super().clean()
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('confirmation')
        if p1 and p2:
            if p1 != p2:
                raise ValidationError("Password not conform")


class loginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


