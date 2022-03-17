from asyncio.windows_events import NULL
from django.db import models

# Create your models here.

class Category(models.Model):
     Category_Name = models.CharField(max_length=200)
     def __str__(self):
         return f"{self.Category_Name}"
     
class Task(models.Model):
     Task_Name = models.CharField(max_length=200)
     Is_Completed = models.BooleanField(default=False)
     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="Task Category", default=NULL)
     def __str__(self):
         return f"{self.Task_Name} in {self.category} is completed is equal to {self.Is_Completed}"