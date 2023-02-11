from django.urls import path

from justforfam.house.views import RoomListView, HouseListView, HouseCreateView, RoomCreateView

app_name = 'house'
urlpatterns = [
    path('homes/', HouseListView.as_view(), name='houses_list'),
    path("homes/create/", view=HouseCreateView.as_view(), name="houses_create"),
    path('home/<str:house_name>/rooms/', RoomListView.as_view(), name='rooms_list'),
    path('home/<str:house_name>/rooms/create/', RoomCreateView.as_view(), name='rooms_create'),
]
