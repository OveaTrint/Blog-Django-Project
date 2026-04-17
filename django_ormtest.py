import setupdjangoORM
from blogs.models import Blog, BlogPost

if __name__ == "__main__":
    blogs = Blog.objects.all()
    blog_post = BlogPost.objects.all()

    g = Blog.objects.all()
    print()
