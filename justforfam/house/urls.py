from django.urls import path

from justforfam.house.views import RoomListView, HouseListView, HouseCreateView, RoomCreateView, HouseDetailView

app_name = 'house'
urlpatterns = [
    path('home/', HouseDetailView.as_view(), name='house_detail'),
    path('neighbours/', HouseListView.as_view(), name='houses_list'),
    path("home/create/", view=HouseCreateView.as_view(), name="houses_create"),
    path('home/<str:house_name>/rooms/', RoomListView.as_view(), name='rooms_list'),
    path('home/<str:house_name>/rooms/create/', RoomCreateView.as_view(), name='rooms_create'),
]
