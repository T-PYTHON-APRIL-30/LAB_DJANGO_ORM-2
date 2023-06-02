from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from .models import Blog
# Create your views here.
def home_page(request:HttpRequest):

    #for searching
    if request.GET.fromkeys("search"):

        search_phrase = request.GET.get("search", "")
        iblogs=Blog.objects.filter(title__contains=search_phrase,)

        return render(request,"main/home_page.html",{"blogs" : iblogs ,"search_phrase":search_phrase})

    blogs =Blog.objects.all()
    return render(request,"main/home_page.html",{"blogs" : blogs})



def add_page(request:HttpRequest):
    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"], contant=request.POST["contant"],  is_published=request.POST["is_published"],publish_date=request.POST["publish_date"])
        new_blog.save()

    return render(request,"main/add_page.html")



def blog_detail(request:HttpRequest,blog_id):
    try:

        iblog=Blog.objects.get(id=blog_id)

    except Exception:

        return HttpResponseNotFound('<h1>page not found!</h1>')

    return render(request,"main/blog_detail.html",{"iblog":iblog})



def blog_update(request:HttpRequest,blog_id):

    iblog=Blog.objects.get(id=blog_id)
    iso_date =iblog.publish_date.isoformat()
    if request.method=='POST':
        iblog.title=request.POST["title"]
        iblog.contant=request.POST["contant"]
        iblog.is_published=request.POST["is_published"]
        iblog.publish_date=request.POST["publish_date"]
        iblog.save()
        return redirect("main:blog_detail",blog_id=iblog.id)
    return render(request,'main/blog_update.html',{"iblog":iblog,"iso_date":iso_date})




def blog_delete(request:HttpRequest,blog_id):
    iblog=Blog.objects.get(id=blog_id)
    iblog.delete()
    return redirect("main:home_page")
