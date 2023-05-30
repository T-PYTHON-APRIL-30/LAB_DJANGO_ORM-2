from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Blog
from datetime import date


# Create your views here.
def home(request: HttpRequest):
    blog = Blog.objects.filter(is_published = True)

    return render(request, 'main_app/home.html', {"blog" : blog})


def post_page(request: HttpRequest):
    if request.method == "POST":
        today = date.today()

        new_blog = Blog(
            title = request.POST["title"],
            content = request.POST["content"],
            is_published = request.POST["is_published"],
            publish_date = today
        )
        new_blog.save()

        return redirect("main_app:home")

    return render(request, 'main_app/post.html')


def detail_page(request: HttpRequest, blog_id):
    blog = Blog.objects.get(id = blog_id)

    return render(request, 'main_app/detail.html', {"blog" : blog})


def update_page(request: HttpRequest, blog_id):
    blog = Blog.objects.get(id = blog_id)
    #iso_date = blog.publish_date.isoformat()

    if request.method == "POST":
        today = date.today()

        blog.title = request.POST["title"]
        blog.content = request.POST["content"]
        blog.is_published = request.POST["is_published"]
        blog.publish_date = today
        blog.save()

        return redirect("main_app:home")

    return render(request, 'main_app/update.html', {"blog" : blog})


def delete_page(request: HttpRequest, blog_id):
    blog = Blog.objects.get(id = blog_id)
    blog.delete()

    return redirect("main_app:home")


def search_page(request: HttpRequest):
    search_phrase = request.GET.get("search", "")
    blog = Blog.objects.filter(title__contains = search_phrase, is_published = True)

    return render(request, 'main_app/search.html', {"blog" : blog})
