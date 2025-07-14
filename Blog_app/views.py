from django.shortcuts import render
from Blog_app.models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
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