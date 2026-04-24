"""Script that generates dummy data for the database"""

import random

import factory
from django.contrib.auth.models import User
from faker import Faker

from blogs.models import Blog, BlogPost

fake = Faker()


def get_title():
    title = " ".join(fake.words()).title()
    return title


def get_description():
    title = " ".join(fake.words(50)).title()
    return title


def get_blog_owner():
    users = User.objects.all()
    return random.choice(users)


class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog

    title = factory.LazyFunction(get_title)
    description = factory.LazyFunction(get_description)
    owner = factory.LazyFunction(get_blog_owner)


class BlogPostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BlogPost

    title = factory.LazyFunction(lambda: " ".join(fake.words()).title())
    body = factory.LazyFunction(
        lambda: "\n\n".join(
            [
                fake.paragraph(random.randint(3, 10))
                for _ in range(random.randint(3, 25))
            ]
        )
    )
    blog = factory.LazyFunction(lambda: random.choice(Blog.objects.all()))
