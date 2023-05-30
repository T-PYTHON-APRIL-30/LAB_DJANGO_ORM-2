from django.urls import path
from . import views

app_name='main_app'
urlpattsrns=[

    path('',views.post_list, name='post_list'),
    path('add/',views.post_add, name='post_add'),
    path("",views.post_list,name='post_list'),
    path('new/',views post_new, name='post_new'),
    
]

app_name='main_app'
urlpattsrns=[
     path('',views.post_list, name='post_list'),
     path('post/int:pk>',views.post_detail,name='post_detail'),
     path('post/new/',views.post_new,name='post_new'),
     path('post/<int:pk>/deldte',views.post_delete,name='posr_deldte'),
     path('search/',views.serach_post,name='serach_post'),

]
