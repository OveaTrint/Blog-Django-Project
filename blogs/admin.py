from django.contrib import admin

from .models import Blog, BlogPost

# lets admin manage the blog model
admin.site.register((Blog, BlogPost))
