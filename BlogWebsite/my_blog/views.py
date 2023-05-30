from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import Blog

# Create your views here.

def show_page(request:HttpRequest):

    blogs = Blog.objects.filter(is_published = True)

    return render(request,"my_blog/show_page.html", {"blogs" : blogs})

def add_page(request:HttpRequest):

    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"], content=request.POST["content"],is_published=request.POST["is_published"])
        new_blog.save()
        return redirect("my_blog:show_page")
    
    return render(request,"my_blog/add_page.html")

def detail_page(request:HttpRequest, blog_id):

    blog = Blog.objects.get( id = blog_id )

    return render(request, 'my_blog/detail_page.html', {"blog" : blog})


def update_page(request:HttpRequest, blog_id):

    blog = Blog.objects.get( id = blog_id )

    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.content = request.POST["content"]
        blog.is_published = request.POST["is_published"]
        blog.save()
        return redirect("my_blog:detail_page", blog_id = blog.id)

    return render(request, 'my_blog/update_page.html', {"blog" : blog})

def delete_blog(request:HttpRequest,blog_id):

    blog = Blog.objects.get(id = blog_id)
    blog.delete()

    return redirect("my_blog:show_page")



def search_page(request:HttpRequest):
    search_phrase = request.GET.get("search", "")
    blogs = Blog.objects.filter(title__contains = search_phrase)

    return render(request, "my_blog/search_page.html", {"blogs" : blogs})