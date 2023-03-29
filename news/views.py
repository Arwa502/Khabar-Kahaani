from django.shortcuts import render, HttpResponse
from .models import Post


# Create your views here.
def newsHome(request): 
    category = request.GET.get('category', None)
    allPosts= Post.objects.all()
    if category:
        allPosts = allPosts.filter(category=category)
    context={'allPosts': allPosts}
    return render(request, "news/newsHome.html", context)

    date = request.GET.get('date', None)
    allPosts= Post.objects.all()
    if category:
        allPosts = allPosts.filter(category=category)
    context={'allPosts': allPosts}
    return render(request, "news/newsHome.html", context)

def newsPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request, "news/newsPost.html", context)