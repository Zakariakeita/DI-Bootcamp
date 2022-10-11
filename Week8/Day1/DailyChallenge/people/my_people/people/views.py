from django.shortcuts import render
from operator import itemgetter
# Create your views here.

people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

def people1(request):
    context={"data":sorted(people, key=itemgetter("age"))}
    return render(request,"people/templates/people1.html",context)

def people2(request,id):
     for key in people:
         for i,j in key.items():
            if i=="id" and j==id:
                #l.append(key)
                context=key 
                print(context)       
     return render(request,"people/templates/people2.html",context)