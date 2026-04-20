from django.contrib.auth import urls as auth_urls
from django.urls import include, path

from . import views

app_name = "accounts"
urlpatterns = [
    path("", include(auth_urls)),
    path("register/", view=views.register, name="register"),
]
