# this a file in the blog app folder
# apps are ways to manage different entities in a project.

from django.contrib.auth.models import User
from django.db import models

# create another manager to print the titles of the books
# class BlogTitleManager(models.Manager):
#     def get_queryset(self):
#         blogs = super().get_queryset().all()
#         for blog in blogs:
#             models.QuerySet()


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    # one blog can have many blogposts
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:50]
