from django.urls import path
from . import models
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('todo/', views.todo, name='todo'),
    path('add/', views.add_todo, name='add_todo'),
    path('update/<int:id>/', views.update_todo, name='update_todo'),
    path('delete/<int:id>/', views.delete_todo, name='delete_todo'),
    path('done/<int:id>/', views.mark_done, name='mark_done'),
    path('logout/', views.logout, name='logout'),
]