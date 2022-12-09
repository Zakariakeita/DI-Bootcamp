from django.shortcuts import render
from .models import Person
from .forms import PhoneForm

# Create your views here.

def phonenumber(request,phone):
    person = Person.objects.get(phone_number = phone)
    return render(request,'phonenumber.html',{'person':person})

def name(request,name):
    person = Person.objects.get(name = name)
    return render(request,'phonenumber.html',{'person':person})


def person(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['number']
            name = form.cleaned_data['name']
            if phone:
                person = Person.objects.get(phone_number = phone)
            else:
                person = Person.objects.get(name = name)
            return render(request,'phonenumber.html',{'person':person})
        return render(request,'search.html',{'form':form})
    else:
        form = PhoneForm()
        return render(request,'search.html',{'form':form})
