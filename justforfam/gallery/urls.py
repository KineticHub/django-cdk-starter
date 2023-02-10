from django.urls import path

from justforfam.gallery.views import ImageView, ImageList, AlbumView, AlbumList, ImageCreate

app_name = 'gallery'
urlpatterns = [
    path('', AlbumList.as_view(), name='album_list'),
    path('images/', ImageList.as_view(), name='image_list'),
    path('image/<str:pk>/<slug>/', ImageView.as_view(), name='image_detail'),
    path('upload/', ImageCreate.as_view(), name='image_upload'),
    path('album/<str:pk>/<slug>/', AlbumView.as_view(), name='album_detail'),
    path('album/<str:apk>/<str:pk>/<slug>', ImageView.as_view(), name='album_image_detail')
]
