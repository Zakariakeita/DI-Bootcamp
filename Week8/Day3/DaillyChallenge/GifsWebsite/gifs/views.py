from django.shortcuts import render
from .models import Categorie,Gif
from .forms import GifForm,CategorieForm
# Create your views here.

def Homepage(request):

    context = {
        'page_title': "Homepage",
        'gifs': Gif.objects.all(),
        'categories':Categorie.objects.all(),

    }
    return render(request, 'home.html', context)


def Add(request):
    context = {
        'page_title' : "Add",
    }

    if request.method == 'POST':
        # POST, generate bound form with data from the request
        form = GifForm(request.POST) # the Person Form
        # check if it's valid:',
        if form.is_valid():
            form.save()
            form_uploader_name = form.cleaned_data['uploader_name']
            form_title = form.cleaned_data['title']
            form_URL = form.cleaned_data['URL']
            form_categorie = form.cleaned_data['categorie']

            context['formInfo'] = {
                    'uploader_name' : form_uploader_name,
                    'title': form_title,
                    'URL': form_URL,
                    'categorie ': form_categorie
                }
            print(context['formInfo'])
            return render(request, 'add.html', context)
        else:
            print("---ERRORS---", form.errors)
            context['form'] = form
            return render(request, 'add.html', context)

    else:
        # GET, generate blank form
        context['form'] = GifForm()
    return render(request, 'add.html', context)

def Categories(request):
    context = {
        'page_title' : "Add",
    }

    if request.method == 'POST':
        # POST, generate bound form with data from the request
        form = CategorieForm(request.POST) # the Person Form
        # check if it's valid:',
        if form.is_valid():
            form.save()
           
            form_categorie = form.cleaned_data['name']

            context['formInfo'] = {
                    
                    'categorie ': form_categorie
                }
            print(context['formInfo'])
            return render(request, 'categories.html', context)
        else:
            print("---ERRORS---", form.errors)
            context['form'] = form
            return render(request, 'categories.html', context)

    else:
        # GET, generate blank form
        context['form'] = CategorieForm()
    return render(request, 'categories.html', context)

#lister les gifs dune categories
def GifsCategorie(request,id):
    context= {
        'id':id,
        'page_title':"GifsCategorie",
        'gifs':Gif.objects.filter(id=id)
    }
    return render(request,'categ.html',context)
#liste categories
def CategoriesGifs(request,id):
    
    gifs=Gif.objects.filter(categorie=id)
    context={
        'gifs':gifs
    }
    return render(request,'categories_gifs.html',context)
def Gif_detail(request,id):
    gif_detail=Gif.objects.filter(id=id)
    context={
        'gifs':gif_detail
    }
    return render(request,'gif_detail.html',context)
