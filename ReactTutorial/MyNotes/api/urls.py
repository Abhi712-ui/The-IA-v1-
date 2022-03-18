from unicodedata import name
from django import urls
from django.urls import path
from . import views

urlpatterns = [
     path('', views.getRoutes, name="routes"),
     path('tasks/', views.getTasks, name="tasks"),
     path('categories/', views.getCategories, name="categories"),
     path('tasks/<str:pk>', views.getTask, name="task"),
     path('categories/<str:pk>', views.getCategory, name="Category")
]