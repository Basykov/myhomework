from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Anything(models.Model):
    something = models.CharField(max_length=10)
    everything = models.CharField(max_length=10)

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    reminders = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title