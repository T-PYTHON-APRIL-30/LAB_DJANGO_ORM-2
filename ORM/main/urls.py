from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('add/', views.add_page, name="add_page"),
    path("blog/detail/<blog_id>/", views.blog_detail, name="blog_detail"),
    path("blog/update/<blog_id>/", views.update_blog, name="update_blog"),
    path("blog/delete/<blog_id>/", views.delete_blog, name="delete_blog"),
    path("blog/search/", views.search_page, name="search_page"),
]
