from django.shortcuts import render
from .models import Contact, Professionals, Post


# Create your views here.
# create the view for teh contact page first
def contactview(request):
    posts = Post.objects.all()
    return render(request, "contact.html", {"posts": posts})
