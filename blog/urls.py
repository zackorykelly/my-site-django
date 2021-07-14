from django.urls import path
from . import views

urlpatterns = [
    path("", views.posts_index, name="posts-index"),
    path("posts", views.posts_list, name="posts-list"),
    path("posts/<slug:slug>", views.posts_detail, name="posts-details")
]
