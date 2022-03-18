from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import Category, Task

class TaskSerializer(ModelSerializer):
     class Meta:
          model = Task
          fields = '__all__'

class CategorySerializer(ModelSerializer):
     class Meta:
          model = Category
          fields = '__all__'