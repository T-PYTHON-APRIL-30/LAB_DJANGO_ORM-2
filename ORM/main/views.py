from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog
# Create your views here.

def home_page(request: HttpRequest):

    blogs = Blog.objects.all()

    return render(request, "main/home_page.html", {"blogs": blogs})

def add_page(request: HttpRequest):
    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"],contant=request.POST["contant"], is_published=request.POST["is_published"], publish_date= request.POST["publish_date"])
        new_blog.save()
        return redirect("main:home_page")
    return render(request, "main/add_page.html")



def blog_detail(request:HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)

    return render(request, 'main/blog_detail.html', {"blog" :blog })


def update_blog(request:HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)

    #updating the blog
    if request.method == "POST":
        Blog.title = request.POST["title"]
        Blog.contant = request.POST["contant"]
        Blog.publish_date = request.POST["publish_date"]
        Blog.is_published = request.POST["is_published"]
        Blog.save()

        return redirect("main:blog_detail", blog_id=blog.id)

    return render(request, 'main/update_blog.html', {"blog" : blog})



def delete_blog(request:HttpRequest, blog_id):
    
    blog = Blog.objects.get(id=blog_id)
    blog.delete()

    return redirect("main:Home_page")


def search_page(request:HttpRequest):
    search_phrase = request.GET.get("search", "")
    blogs = Blog.objects.filter(title__contains=search_phrase,)

    return render(request, "main/search_page.html", {"blogs" : blogs})