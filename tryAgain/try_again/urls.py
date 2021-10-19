# from django.urls import path,include
# from .views import home ,about , service , contact 

from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name='index'),
    path('contact/', views.contact,name='contact'),
    path('service/', views.services,name='services'),
    path('about/', views.about,name='about'),
    path('', views.user_registration,name='registration'),
    path('login', views.user_login,name='login'),
    path('logout', views.user_logout,name='logout'),
    path('Post_blog', views.post_blog,name='post_blog'),
    path('blog_detail/<int:id>', views.blog_detail,name='blog_detail'),
]