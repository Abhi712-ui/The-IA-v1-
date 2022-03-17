from unicodedata import name
from django import urls
from django.urls import path
from . import views

urlpatterns = [
     path('', views.getRoutes, name="routes"),
     path('tasks/', views.getTasks, name="tasks")
     path('categories/', views.getCategories, name="categories")
]