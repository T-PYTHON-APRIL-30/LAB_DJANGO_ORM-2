from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog

# Create your views here.

def home(request:HttpRequest):

    blogs = Blog.objects.all()

    return render(request, 'main_app/home.html', {'blogs' : blogs})

def add_blog(request:HttpRequest):

    if request.method == 'POST':
        new_blog = Blog(title = request.POST['title'], content = request.POST['content'],is_published=request.POST["is_published"], publish_date = request.POST['publish_date'])
        new_blog.save()
        return redirect('main_app:home')

    return render(request, 'main_app/add.html', )

def detail(request:HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)

    return render(request, 'main_app/detail.html', {'blog': blog})

def update_blog(request:HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)
    iso_date = blog.publish_date.isoformat()

    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.content = request.POST['content']
        blog.is_published = request.POST['is_published']
        blog.publish_date = request.POST['publish_date']
        blog.save()

        return redirect('main_app:detail', blog_id= blog.id)

    return render(request, 'main_app/update.html',{'blog': blog, 'iso_date' : iso_date} )

def delete(request:HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    
    return redirect('main_app:home')

def search(request:HttpRequest):
    search_phrase = request.GET.get("search", "")
    blogs = Blog.objects.filter(title__contains=search_phrase,)

    return render(request, "main_app/search.html", {"blogs" : blogs})