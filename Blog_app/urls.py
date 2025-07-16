from django.urls import path
from Blog_app import  views

urlpatterns = [
    path("",views.post_list, name="post-list"),
    path('details/<int:pk>/',views.post_details , name="post-detail"),
    path('draft/',views.post_list , name='draft-list'),
]