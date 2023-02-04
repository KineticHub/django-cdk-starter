from django.shortcuts import render
from django.views import View


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
