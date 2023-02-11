from django.urls import path

from justforfam.posts.views import PostsListView, PostView, PostCreateView

app_name = 'posts'
urlpatterns = [
    path('posts/', PostsListView.as_view(), name='posts_list'),
    path('posts/create/', PostCreateView.as_view(), name='posts_create'),
    path('post/<str:post_title>/<str:pk>/', PostView.as_view(), name='post_view'),
]
