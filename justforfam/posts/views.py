from django.shortcuts import render
from django.views import View


class PostsListBaseView(View):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


posts_list_view = PostsListView.as_view()
