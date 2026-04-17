from django.shortcuts import render

from .models import Blog, BlogPost

"""VIEW FUNCTIONS: What users can see when they access the correspondng page's url"""


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
