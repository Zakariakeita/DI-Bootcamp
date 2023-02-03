from django.urls import path,include
from . import views

urlpatterns = [
    path('add/', views.todo, name ='add_todo'),
    path('add/<int:id>', views.user_todo, name ='add_user_todo'),
    path('display/', views.display_todos,name ='display_todos'),
    path('display_user_todos/<int:id>', views.display_user_todos,name ='display_user_todos'),
    
    path('category/<str:name>', views.category,name ='category'),

    path('todo_done/<int:id>', views.todo_done,name ='todo_done'),
    path('clear_all/', views.clear_all,name ='clear_all'),
    path('delete_todo/<int:id>', views.delete_todo,name ='delete_todo'),

    path('login/', views.login,name ='login'),
    path('signup/', views.signup,name ='signup'),
]  