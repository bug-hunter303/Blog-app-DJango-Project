from django.shortcuts import render
from Blog_app.models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_at__isnull = False) # data vako
    # posts = Post.objects.exclude(published_at = None)
    return render(
        request,
        "post_list.html",
        {"posts": posts},
    )
    
def post_details(request,pk):
    post = Post.objects.get(pk=pk) # pk = primary key same as id 
    return render(
        request,
        "post_detail.html",
        {"post": post},
    )
    
@login_required
def draft_list(request):
    posts = Post.objects.filter(published_at__isnull = True) # data vako
    # posts = Post.objects.exclude(published_at = None)
    return render(
        request,
        "draft_list.html",
        {"posts": posts},
    )
    
@login_required
def draft_detail(request , pk):
    post = Post.objects.get(pk=pk , published_at__isnull = True)
    return render(
        request,
        "draft_detail.html",
        {"post": post},
    )

# def draft_publish(request,pk):
    post = Post.objects.get(pk = pk , published_at__isnull = True)
    return render(
        request,
        'post-list.html',
        {'posts': post},
    )
    

    
    