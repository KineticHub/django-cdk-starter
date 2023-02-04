from django.urls import path

from justforfam.house.views import RoomListView, HouseListView

app_name='house'
urlpatterns = [
    path('homes/', HouseListView.as_view(), name='houses_list'),
    path('home/<str:house_name>/rooms/', RoomListView.as_view(), name='rooms_list'),
]
