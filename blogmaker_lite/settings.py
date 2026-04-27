import os
from pathlib import Path

# settings for django
# ROOT_URLCONF tells django where to look for URLs to listen for
# DEBUG is whether a not logs should be shown
# secret_key is to safeguard your backend when during deployment

os.environ.setdefault("PGDATABASE", "blogs")
os.environ.setdefault("PGUSER", "postgres")
os.environ.setdefault("PGPASSWORD", "kamal265")
os.environ.setdefault("PGHOST", "localhost")
os.environ.setdefault("PGPORT", "5432")

BASE_DIR = Path(__file__).resolve().parent.parent
ALLOWED_HOSTS = ["*"]

WSGI_APPLICATION = "blogmaker_lite.wsgi.application"
ROOT_URLCONF = "blogmaker_lite.urls"
DEBUG = False
SECRET_KEY = "my_secret_key"
TEMPLATES = [
    {
        # specifies which template backend we should use
        # template backends help generate dynamic html
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # path of where the template files are
        "DIRS": [Path(__file__).parent / "templates"],
        # tells django to look within apps for templates too
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    },
]
INSTALLED_APPS = [
    "blogs",
    "accounts",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
]

# responsible for processing user's request
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["PGDATABASE"],
        "USER": os.environ["PGUSER"],
        "PASSWORD": os.environ["PGPASSWORD"],
        "HOST": os.environ["PGHOST"],
        "PORT": os.environ["PGPORT"],
    }
}

# defines how to manage auto-incrementing fields
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# tells django how to generate a url for static files, add the url path to the beginning of each static file
# e.g static/custom.css, static/chota.css
STATIC_URL = "static/"

# directories that contain static files that are the same for all users
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "css"),
    os.path.join(BASE_DIR, "static"),
]
# where django should store all static files it finds with the collectstatic command
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# tells django to redirect users to blog/index.html after authenciation"
LOGIN_REDIRECT_URL = "blogs:index"
LOGOUT_REDIRECT_URL = "blogs:index"
