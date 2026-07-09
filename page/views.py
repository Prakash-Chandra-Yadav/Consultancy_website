from django.shortcuts import render
from .models import Contact, Professionals, Post
from django.views.generic import ListView


# Create your views here.
# create the view for teh contact page first
def contactview(request):
    contacts = Contact.objects.all()
    return render(request, "contact.html", {"contacts": contacts})


# this retuens the view of the contact us page and the professionals database objects
def aboutView(request):
    professionals = Professionals.objects.all()
    return render(request, "about.html", {"professionals": professionals})


def homeview(request):
    return render(request, "home.html")


def projectview(request):
    return render(request, "projects.html")
