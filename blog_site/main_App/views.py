from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from.models import post
from models import PostForm



# Create your views here.

def add_post(request:HttpRequest):
    if request.method == "POST":
            new_blog =new_blog(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"], publish_date=request.POST["publish_date"])
            new_blog.save()
            return redirect("main_app:add_post")
    return render (request, "main_app/add_blog.html")

def post_add(request:HttpRequest):

   
    return render(request, "main_app/post_add.html")  

def add_post(request:HttpRequest):
     add_post=post.objects.filter(published_date_isnull=False)
     return render(request, 'blog/add_post.html',{add_post:post})

def add_pos_new(request:HttpRequest):
     if request.method=='POST':
          #handel from submissions
            pass
     else:
          #display empty form
          pass
     return render(request, 'blog/add_post_edit.html')


def post_list(request:HttpRequest):
     posts=post_list.object.filter(is_published=True)
     return render(request, 'blog/post_list.html',{'posts':post})

def post_detail(request,PK):
     post=get_object_or_404(post_list, PK=PK)
     return render(request, ' blog/post_detail.html',{'posts':post})


def post_new(request):
     if request.method =='POST':
          form =PostForm(request.POST)
          if form.is_valid():
               post=form.save(commit=False)
               post.save()
               return redirect('post_detail', pk=post.pk)
     else:
          form=PostForm()
          return render(request, ' blog/post_edit.html',{'posts':post})
     

def post_edit(request, pk):
     post=get_object_or_404(post,pk=pk)
     if request.method=='POST':
          form=PostForm(request.POST,isinstance=post)
          if form.is_valid():
               post=form.save(commit=False)
               post.save()
               return redirect('post_detail',pk=post.pk)
          else:
               form=PostForm(isinstance=post)
               return render(request, ' blog/post_edit.html',{'posts':post})
          
def post_delete(request,pk):
     post=get_object_or_404(post, pk=pk)
     return redirect('post_list')


def search_post(request):
     query=request.GET.get('q')
     if query:
          post_list=post.objects.filter(title__icontains=query,is_published=True)
          return render(request, 'blog/post_list.html',{post_list:post_list})
     else:
          return redirect ('post_list')
     


