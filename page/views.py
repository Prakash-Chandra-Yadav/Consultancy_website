from django.shortcuts import render
from .models import Contact, Professionals, Post


# Create your views here.
# create the view for teh contact page first
def contactview(request):
    contacts = Contact.objects.all()
    return render(request, "contact.html", {"contacts": contacts})
