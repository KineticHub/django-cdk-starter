from urllib.parse import unquote

from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView

from justforfam.core.utils.permissions import ExtendedAutoPermissionRequiredMixin
from justforfam.house.models import House, Room
from justforfam.posts.models import Post


class PostsListView(ExtendedAutoPermissionRequiredMixin, ListView):
    model = Post
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        house = get_object_or_404(House, name=unquote(self.kwargs['house_name']), family__in=[self.request.user])
        room = get_object_or_404(Room, name=unquote(self.kwargs['room_name']), house=house)
        return Post.objects.filter(room=room)


class PostView(ExtendedAutoPermissionRequiredMixin, DetailView):
    model = Post
    template_name = 'posts/post_viewer.html'
    context_object_name = 'post'


# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()
#
#     return render(request, 'name.html', {'form': form})
#
# def TextPostsView(request, object_id, template_name='locations/location_details.html'):
#     location = LocationModel.objects.get(id=object_id)
#     context = {'location':location}
#     return render(request, template_name, context)
#
# class PostsListBaseView(View):
#     model = User
#     slug_field = "username"
#     slug_url_kwarg = "username"
#
#
# posts_list_view = PostsListView.as_view()
