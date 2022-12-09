from django.shortcuts import render,redirect, HttpResponse
from todo.forms import AddTodoForm,loginForm,signupForm
from todo.models import *
from django.utils import timezone
from django.contrib import messages


# Create your views here.


def todo(request):
    if request.method == 'POST':
        form = AddTodoForm(request.POST)
        if form.is_valid():
            todo = Todo.objects.create(
                title = form.cleaned_data['title'],
                details = form.cleaned_data['details'],
                deadline_date = form.cleaned_data['deadline_date'],
                category = Category.objects.get(id = form.cleaned_data['category'])
            )
            todo.save()
            return redirect('display_todos')
        return render(request,'todo.html',{'form':form})
    else:
        form = AddTodoForm()
    return render(request,'todo.html',{'form':form})


def user_todo(request,id):
    if request.method == 'POST':
        form = AddTodoForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=id)
            todo = user.users.create(
                title = form.cleaned_data['title'],
                details = form.cleaned_data['details'],
                deadline_date = form.cleaned_data['deadline_date'],
                category = Category.objects.get(id = form.cleaned_data['category'])
            )
            todo.save()
            return redirect('display_user_todos', user.id)
        return render(request,'todo.html',{'form':form})
    else:
        form = AddTodoForm()
    return render(request,'todo.html',{'form':form})


def display_todos(request):
    todos = Todo.objects.all()
    done = Todo.objects.filter(has_been_done = True)
    uncomplete = Todo.objects.filter(has_been_done = False)
    t_done = done.count()
    t_uncomplete = uncomplete.count()
    context  = {
        'todos' : todos,
        'done' : done,
        'uncompleted' : uncomplete,
        't_done' : t_done,
        't_uncomplete' : t_uncomplete
    }
    return render(request,'display_todos.html',context)


def todo_done(request,id):
    todo = Todo.objects.get(id=id)
    todo.has_been_done = True
    todo.date_completion = timezone.now()
    todo.save()
    if todo.congratule():
            messages.success(request, f'Congratulation ! You succeed the mission')
    return redirect('display_todos')


def category(request,name):
    try:
        category = Category.objects.get(name = name)
        todos = category.category.all()
        n = todos.count()
    except:
        return HttpResponse('<h1 style = "color:red;">Category not found</h1>')
    return render(request,'category.html',{'category':category, 'todos':todos,'ntask':n})

def clear_all(request):
    todos = Todo.objects.all().delete()
    return redirect('display_todos')

def delete_todo(request,id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('display_todos')

def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('display_user_todos', user.id)
        return render(request,'signup.html',{'form':form})
    else:
        form = loginForm()
    return render(request,'signup.html',{'form':form})


def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username = form.cleaned_data.get('username'))
            if user.password == form.cleaned_data.get('password'):
                return redirect('display_user_todos',user.id)
            messages.success(request, f'Password or username not correct')
            return render(request,'login.html',{'form':form})
        return render(request,'login.html',{'form':form})
    else:
        form = loginForm()
    return render(request,'login.html',{'form':form})

def display_user_todos(request,id):
    try:
        user = User.objects.get(id=id)
    except :
        return HttpResponse(f'<h1 style = "color:red;">Not a valid user</h1>')

    todos = user.users.all()
    done = user.users.filter(has_been_done = True)
    uncomplete = user.users.filter(has_been_done = False)
    t_done = done.count()
    t_uncomplete = uncomplete.count()
    context  = {
        'todos' : todos,
        'done' : done,
        'uncompleted' : uncomplete,
        't_done' : t_done,
        't_uncomplete' : t_uncomplete,
        'user': user
    }
    return render(request,'display_todos.html',context)

  