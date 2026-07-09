from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
# create the model for the post
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length=50)
    position = models.CharField(max_length=50, default="Employee")
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


# create the model for the contact details
class Contact(models.Model):
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        """returns the location as the string so that i can be seen on the admin panel"""
        return self.location


# create the model to store the professionals details
class Professionals(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    experience = models.CharField(max_length=100, default="Expert")
    image = models.ImageField(upload_to="professionals/")

    def __str__(self):
        """returns the name of the employee so that it can be seen of the website"""
        return self.name
