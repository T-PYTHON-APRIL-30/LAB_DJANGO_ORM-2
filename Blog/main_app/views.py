from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Post
import requests

# Create your views here.

def homePage (request:HttpRequest):
    posts = Post.objects.filter(is_published=True)
    return render(request, "main_app/home.html", {"posts" : posts})
    
     
def postsPage(request):

    if request.method == "POST":
            
        newPost= Post(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"], publish_date=request.POST["publish_date"])
        newPost.save()
        return redirect("main_app:homePage")
    
    return render (request,'main_app/post.html') 

def detailsPage(request:HttpRequest,post_id):
    #الأفضل نحطها في تراي واكسبت لأن لو ما حصل الأيدي بيرجع ايرور

    post = Post.objects.get(id = post_id)
    return render(request,'main_app/post_details.html',{'post': post})

    '''try:
        response = requests.get(f'http://127.0.0.1:8000/posts/details/{post_id}/')

        if response.status_code == 200:
        post = Post.objects.get(id = post_id)
        return render(request,'main_app/post_details.html',{'post': post})
    
    except ValueError:
        return redirect(("main_app:notFoundPage"))'''

def updatePage(request:HttpRequest,post_id):

    post = Post.objects.get(id= post_id)

     #updating the post
    if request.method == "POST":

        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.publish_date = request.POST["publish_date"]
        post.is_published = request.POST["is_published"]
        post.save()

        return redirect("main_app:detailsPage", post_id=post.id)
    
    return render(request,'main_app/update_post.html',{'post': post})

def searchPage(request:HttpRequest):
    search_phrase = request.GET.get("search", "")
    posts = Post.objects.filter(title__contains=search_phrase)

    return render(request, "main_app/search.html", {"posts" : posts})

def deletePost(request:HttpRequest, post_id):
    
    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect("main_app:homePage")

def notFoundPage (request:HttpRequest, post_id):
    post = Post.objects.get(id = post_id)    
    return render (request,"main_app/notFound.html",{'post': post})

