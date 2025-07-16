from django.urls import path
from Blog_app import  views

urlpatterns = [
    path("",views.post_list, name="post-list"),
    path('details/<int:pk>/',views.post_details , name="post-detail"),
    path('draft/',views.draft_list , name='draft-list'),
    path('detail/<int:pk>/',views.draft_detail , name='draft-detail'),
]