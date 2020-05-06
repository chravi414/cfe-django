from django.urls import path
from posts.views import posts_list, posts_detail, post_create, post_update, post_delete

urlpatterns = [
    path('', posts_list, name='post_list'),
    path('<int:id>', posts_detail, name="post_detail"),
    path('update/<int:id>', post_update, name='post_update'),
    path('create', post_create, name="post_create"),
    path('delete/<int:id>', post_delete, name="post_delete")
]
