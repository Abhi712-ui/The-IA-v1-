from unicodedata import name
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Category(models.Model):
     name = models.CharField(max_length=200, null=True, blank=True)

class Task(models.Model):
     category = models.ForeignKey(Category, on_delete=models.CASCADE)
     task_name = models.CharField(max_length=200, null=True, blank=True)
     due_date = models.DateTimeField(null=True)
     date_created = models.DateTimeField(auto_now_add=True)
     priority = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
     is_completed = models.BooleanField(default=False)
