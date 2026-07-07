from django.contrib import admin
from .models import Post, Contact, Professionals

# Register your models here.
# register all the models on the admin page so that i can be seen there
admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Professionals)
