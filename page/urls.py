from django.urls import path
from .views import contactview, aboutView

urlpatterns = [
    path("", contactview, name="contact"),
    path("about/", aboutView, name="about"),
]
