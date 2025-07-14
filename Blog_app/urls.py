from django.urls import path
from Blog_app import  views

urlpatterns = [
    path("",views.post_list, name="post-list"),
]