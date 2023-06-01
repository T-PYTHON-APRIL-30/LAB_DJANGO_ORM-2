from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse,HttpResponseNotFound
from django.shortcuts import resolve_url
from .models import blog
# Create your views here.

def home_page(request:HttpRequest):
    
    #for searching
    if "search" in request.GET:
        
        search_phrase = request.GET["search"]
        iblogs=blog.objects.filter(title__contains=search_phrase,)
        return render(request,"main_app/index.html",{"blogs" : iblogs ,"search_phrase":search_phrase})
    

    if "is_published" in request.GET:
            ispublished = request.GET["is_published"]
            iblogs=blog.objects.filter(is_published=ispublished)
            return render(request,"main_app/index.html",{"blogs" : iblogs })
      
    blogs =blog.objects.all()
    return render(request,"main_app/index.html",{"blogs" : blogs})






def add_page(request:HttpRequest):
    if request.method == "POST":
        
        new_blog = blog(title=request.POST["title"], Content=request.POST["Content"],  is_published=request.POST["is_published"],publish_date=request.POST["publish_date"],image=request.FILES["image"])
        new_blog.save()
    return render(request,"main_app/add.html")

def blog_detail(request:HttpRequest,blog_id):
    try:

        iblog=blog.objects.get(id=blog_id)
    except Exception:
        return HttpResponseNotFound('<h1>page not found!</h1>')

    return render(request,"main_app/detail.html",{"iblog":iblog})

def blog_update(request:HttpRequest,blog_id):

    iblog=blog.objects.get(id=blog_id)
    iso_date =iblog.publish_date.isoformat()
    if request.method=='POST':
        iblog.title=request.POST["title"]
        iblog.Content=request.POST["Content"]
        iblog.is_published=request.POST["is_published"]
        iblog.publish_date=request.POST["publish_date"]
        if "image" in request.FILES:
            iblog.image=request.FILES["image"]
        iblog.save()
        return redirect("main_app:blog_detail",blog_id=iblog.id)
    return render(request,'main_app/update.html',{"iblog":iblog,"iso_date":iso_date})

def blog_delete(request:HttpRequest,blog_id):
    iblog=blog.objects.get(id=blog_id)
    iblog.delete()
    return redirect("main_app:home_page")
