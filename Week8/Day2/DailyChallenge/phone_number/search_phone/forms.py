from .models import Person
from django import forms
from phonenumber_field.formfields import PhoneNumberField

class PhoneForm(forms.Form):
    number = PhoneNumberField(region="BF",required = False)
    name = forms.CharField(required =False)