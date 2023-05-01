from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.newsHome, name="newsHome"),
    path('addPost', views.addPost, name="addPost"),
    path('<str:slug>', views.newsPost, name="newsPost"),
    path('post/<int:sno>/delete/', views.delete_post, name='delete_post')
    
]