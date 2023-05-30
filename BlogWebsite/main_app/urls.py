from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add_blog, name='add'),
    path('update/<blog_id>/', views.update_blog, name='update'),
    path('detail/<blog_id>/', views.detail, name='detail'),
    path('delete/<blog_id>/', views.delete, name='delete'),
    path('search', views.search, name='search'),
]