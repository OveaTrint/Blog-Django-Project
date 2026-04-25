from django.contrib import admin
from django.urls import include, path

# URLs the django server listens for, "" is by default localhost:8000
# So path("", index) means when localhost:8000 is accessed, index is shown
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", include("blogs.urls")),
]
