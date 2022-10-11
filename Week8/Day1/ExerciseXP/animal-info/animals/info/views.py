from itertools import count
from multiprocessing import context
from django.shortcuts import render

# Create your views here.
mydict={
    "animals": [
        {
            "id" :1,
            "name": "Dog",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2
        },
        {
            "id": 2,
            "name": "Domestic Cat",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1
        },
        {
            "id": 3,
            "name": "Panther",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1 
        },
        {
            "id": 4,
            "name": "Elephant",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 3 
        },
         {
            "id": 5,
            "name": "Snake",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 4 
        },
         {
            "id": 6,
            "name": "bee",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 5 
        }
    ],
    "families": [
        {
            "id": 1,
            "name": "Felidae"
        },
        {
            "id": 2,
            "name": "Caninae"
        },
        {
            "id": 3,
            "name": "Mammal"
        },
        {
            "id": 4,
            "name": "Reptile"
        },
        {
            "id": 5,
            "name": "Insect"
        }
    
    ]
    }
def family(request,id):
    
    l=[]
    for key in mydict:
        if key=="animals":
            for i in mydict[key] :
                for j in i :
                    if j=="family" :
                        if i[j]==id:
                            l.append(i)
    context={"data":l}
    return render(request,"info/templates/family.html",context)

def animals(request,id):
     for key in mydict:
        if key=="animals":
            for i in mydict[key] :
                for j in i :
                    if j=="id" :
                        if i[j]==id :
                            context=i
                            return render(request,"info/templates/animals.html",context)

