from django.urls import path

from . import views

app_name = "blogs"
# URLs the django server listens for, "" is by default localhost:8000
# So path("", index) means when localhost:8000 is accessed, index is shown
urlpatterns = [
    path("blogs/", views.blogs, name="blogs"),
    path("blogs/<int:blog_id>/", views.blog, name="blog"),
    path("posts/<int:post_id>/", views.post, name="post"),
    path("new_blog/", views.new_blog, name="new_blog"),
    path("new_post/<int:blog_id>", views.new_post, name="new_post"),
    path("", views.index, name="index"),
]
