from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.newsHome, name="newsHome"),
    path('<str:slug>', views.newsPost, name="newsPost"),
]