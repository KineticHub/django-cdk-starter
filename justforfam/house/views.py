from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from justforfam.core.utils.permissions import ExtendedAutoPermissionRequiredMixin
from justforfam.house.models import Room, House


class HouseListView(ExtendedAutoPermissionRequiredMixin, ListView):
    model = House
    template_name = 'house/house_list.html'
    context_object_name = 'houses_list'

    def get_queryset(self):
        return House.objects.filter(family__in=[self.request.user])


class RoomListView(ExtendedAutoPermissionRequiredMixin, ListView):
    model = Room
    template_name = 'house/room_list.html'
    context_object_name = 'rooms_list'

    def get_queryset(self):
        house = get_object_or_404(House, name=self.kwargs['house_name'], family__in=[self.request.user])
        return Room.objects.filter(house=house)
