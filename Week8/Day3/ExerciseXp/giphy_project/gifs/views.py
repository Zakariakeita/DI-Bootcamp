from urllib.request import urlopen,Request
from django.shortcuts import render,redirect,HttpResponse
from .models import Gif,Category
from .forms import GifForm,CategoryForm
from django.contrib import messages
import json


# Create your views here.

def homepage(request):
    gifs = Gif.objects.all()
    context = {
        'gifs' : gifs
    }
    return render(request,'homepage.html',context)

def add_new_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            category = form.cleaned_data.get('name')
            print(category)
            messages.success(request, f'New Category created!')
            return redirect('gifs.homepage')
    else:
        form = CategoryForm()
    return render(request,'category.html',{'form':form})

def add_new_gif(request):
    if request.POST:
        form = GifForm(request.POST)
        if form.is_valid():
            gif = form.save(commit=False)
            print(gif)
            gif.save()
            form.save_m2m()
            categories = form.cleaned_data.get('categories')
            print(categories)
            for category in categories:
                gif.categories.add(category)

            messages.success(request, f'New Gif created with success')
            return redirect('gifs.homepage')
    else:
        form = GifForm()
    return render(request,'gifs.html',{"form":form})

def category(request,id):
    c1 = Category.objects.get(id=id)
    context = {
        'gifs':c1.gifs.all()
    }
    return render(request,'category_gifs.html',context)

def gif(request,id):
    c1 = Gif.objects.get(id=id)
    return render(request,'gif.html',{'gif':c1})

def categories(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request,'all_categories.html',context)

def populate(request):
    q = "trending"
    limit = 10
    key = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
    url = f"https://api.giphy.com/v1/gifs/search?q={q}&rating=g&api_key={key}&limit={limit}&tag=hilarous"

    with urlopen(url) as response:
        data = json.loads(response.read())
    # liste = []
    category = Category.objects.create(name = q)
    # category.save()
    for ele in data['data']:
        g = Gif.objects.create(title = ele['title'], url =  ele['images']['downsized']['url'],uploader_name = "Abdoul G")
        category.gifs.add(g)
    
    return redirect('gifs.homepage')
     
def like(request,like_id):
    gif = Gif.objects.get(pk=like_id)
    gif.likes += 1
    gif.save()
    print(gif.likes)
    return render(request,'gif.html',{'gif':gif})


def dislike(request,dislike_id):
    gif = Gif.objects.get(pk=dislike_id)
    gif.likes -= 1
    gif.save()
    print(gif.likes)
    return render(request,'gif.html',{'gif':gif})

def totallike(request):
    gifs = Gif.objects.filter(likes__gt = 0 ).order_by('-likes').values()
    return render(request,'totallike.html',{'gifs':gifs})

