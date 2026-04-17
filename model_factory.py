"""Script that generates dummy data for the database"""

import random

import factory
from faker import Faker

from blogs.models import Blog, BlogPost

fake = Faker()


class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog

    title = factory.LazyFunction(lambda: " ".join(fake.words()).title())
    description = factory.LazyFunction(lambda: " ".join(fake.words(nb=15)).capitalize())


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
