from django.urls import path
from posts.views import posts_list, posts_detail, post_create

urlpatterns = [
    path('', posts_list, name='home'),
    path('<int:id>', posts_detail, name="post_detail"),
    path('create', post_create, name="post_create")
]
