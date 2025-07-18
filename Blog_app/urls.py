from django.urls import path
from Blog_app import  views

urlpatterns = [
    path("",views.post_list, name="post-list"),
    path('details/<int:pk>/',views.post_details , name="post-detail"),
    path('draft/',views.draft_list , name='draft-list'),
    path('detail/<int:pk>/',views.draft_detail , name='draft-detail'),
    path('create/',views.post_create , name="post-create"),
    path('post-update/<int:pk>/', views.post_update , name="post-update"),
    path('post-publish/<int:pk>/', views.post_publish, name="post-publish"),
    path('post-delete/<int:pk>/',views.post_delete, name="post-delete")
]