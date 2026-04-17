import django
from django.conf import settings

settings.configure(
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "blogs",
            "USER": "postgres",
            "PASSWORD": "kamal265",
            "HOST": "localhost",
            "PORT": "5432",
        }
    },
    INSTALLED_APPS=[
        "blogs",
    ],
)

django.setup()
