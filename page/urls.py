from django.urls import path
from .views import contactview, aboutView, homeview, projectview

urlpatterns = [
    path("", homeview, name="home"),
    path("about/", aboutView, name="about"),
    path("contact/", contactview, name="contact"),
    path("projects/", projectview, name="projects"),
]
