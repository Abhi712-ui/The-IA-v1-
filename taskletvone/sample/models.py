from django.db import models

# Create your models here.

class Task(models.Model):
     Task_Name = models.CharField(max_length=200)
     Is_Completed = models.BooleanField(default=False)

class Category(models.Model):
     Category_Name = models.CharField(max_length=200)
     