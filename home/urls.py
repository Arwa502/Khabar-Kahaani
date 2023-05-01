from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('login/', views.loginUser, name = 'login'),
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('search', views.search, name="search"),
    path('signup', views.signupUser, name="signup"),
    path('logout', views.LogoutUser, name="logout"),
]
