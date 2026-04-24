import os

import django
from django.contrib.auth.models import User

from blogs.models import Blog, BlogPost

if __name__ == "__main__":
    os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
    django.setup()

    blogs = Blog.objects.all()
    blog_post = BlogPost.objects.all()

    users = User.objects.all()
    for user in users:
        print(user.id)
        print(user.username)
