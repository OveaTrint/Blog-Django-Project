from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView

from .forms import BlogForm, BlogPostForm
from .models import Blog, BlogPost

"""VIEW FUNCTIONS: What users can see when they access the corresponding page's url"""


# The response returned when a request is made to index
def index(request):
    # Renders response from index.html
    return render(request, "blogs/index.html")


def blogs(request):
    all_blogs = Blog.objects.all()
    context = {"blogs": all_blogs}

    return render(request, "blogs/blogs.html", context=context)


def blog(request, blog_id: int):
    blog = Blog.objects.get(id=blog_id)
    blog_posts = blog.blogpost_set.all()

    context = {
        "blog": blog,
        "blog_posts": blog_posts,
    }

    return render(request, "blogs/blog.html", context=context)


def post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    blog = post.blog

    context = {
        "post": post,
        "blog": blog,
    }
    return render(request, "blogs/post.html", context=context)


@login_required
def new_blog(request):
    if request.method != "POST":
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()

            return redirect("blogs:blogs")
    context = {"form": form}

    return render(request, "blogs/new_blog.html", context)


@login_required
def new_post(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    allowed_guests = ["kamal", "jason", "tayo", "joseph"]

    if request.user not in allowed_guests or request.user != blog.owner:
        return HttpResponse("<h1>403 forbidden</h1> ")

    if request.method != "POST":
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.save()

            return redirect("blogs:blog", blog_id)

    context = {"form": form, "blog": blog}
    return render(request, "blogs/new_post.html", context)
