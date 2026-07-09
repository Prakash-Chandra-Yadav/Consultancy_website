from django.urls import path
from .views import contactview, aboutView, homeview, projectview, project_details

urlpatterns = [
    path("", homeview, name="home"),
    path("about/", aboutView, name="about"),
    path("contact/", contactview, name="contact"),
    path("projects/", projectview, name="projects"),
    path("projects/<int:pk>/", project_details, name="project_details"),
]
