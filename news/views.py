from django.shortcuts import render, redirect, get_object_or_404
from news.models import Post
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.
def newsHome(request): 
    category = request.GET.get('category', None)
    selected_date = request.GET.get('date', None)
    allPosts= Post.objects.all()
        
    if category:
            allPosts = allPosts.filter(category=category)
    if selected_date:
        allPosts = allPosts.filter(publish_date__date=selected_date)
    
    context={'allPosts': allPosts}
    return render(request, "news/newsHome.html", context)


def newsPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request, "news/newsPost.html", context)


@login_required(login_url='login')
def addPost(request):
    if request.method=="POST":
        title=request.POST['title']
        author=request.POST['author']
        slug=request.POST['slug']
        content =request.POST['content']
        category = request.POST['category']
        
        post=Post(title=title, author=author, slug=slug, content=content, category=category)
        post.save()
        messages.success(request, "Your post has been successfully saved")
    
    return render(request, "news/addPost.html")

@login_required(login_url='login')
def delete_post(request, sno):
    post = get_object_or_404(Post, sno=sno)
    if request.user == post.user:
        post.delete() # or save edits
        messages.success(request, "Successfully Deleted")
        #post = get_object_or_404(Post, sno=sno)
    #post.delete()

    elif request.user !=post.user: 
        messages.error(request, "You are not the owner of this post. You can not delete this post")
    
    return redirect ('newsHome')