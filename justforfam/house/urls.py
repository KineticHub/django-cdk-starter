from django.urls import path

from justforfam.house.views import RoomListView, HouseListView

urlpatterns = [
    path('homes/', HouseListView.as_view()),
    # path('home/<house_name>/', RoomListView.as_view()),
    path('home/<house_name>/rooms/', RoomListView.as_view()),
]
