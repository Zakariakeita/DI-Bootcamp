from itertools import count
from multiprocessing import context
from django.shortcuts import render
from .models import Animal,Famille
# Create your views here.


def family(request,id):
    animals=Animal.objects.filter(family_id=id)
    context={"data":animals}
    return render(request,"info/templates/family.html",context)

def animals(request,id):
     animals=Animal.objects.get(id=id)
     
     context={"data":animals}
     return render(request,"info/templates/animals.html",context)


def animalslist(request):
    animal=Animal.objects.all()
     
    context={"data":animal}
    return render(request,"info/templates/animalslist.html",context)
