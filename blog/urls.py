from django.urls import path
from .views import *
urlpatterns = [
    path('posts',post_list ,name='post-list'),
    path('detail/<int:post_id>',post_detail ,name='post-detail'),
    path('authors',auther_list ,name='post-authors-list'),
    path('authors/<str:author_name>', author_post,name='author-post'),
]