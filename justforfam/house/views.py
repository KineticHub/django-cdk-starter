from urllib.parse import unquote

from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView

from justforfam.core.utils.permissions import ExtendedAutoPermissionRequiredMixin
from justforfam.house.models import Room, House
from justforfam.house.utils.room_utils import RoomDefinitions


class HouseDetailView(ExtendedAutoPermissionRequiredMixin, DetailView):
    model = House
    template_name = 'house/house_detail.html'

    def get_object(self, queryset=None):
        return self.request.user.house


class HouseListView(ExtendedAutoPermissionRequiredMixin, ListView):
    model = House
    template_name = 'house/house_list.html'
    context_object_name = 'houses_list'

    def get_queryset(self):
        return {
            'neighbors': House.objects.filter(neighbours__in=[self.request.user])
        }


class HouseCreateView(ExtendedAutoPermissionRequiredMixin, CreateView):
    model = House
    fields = ['name', 'cover_image']

    def form_valid(self, form):
        form.save()

        # add the current user to the house family
        form.instance.family.add(self.request.user)

        # create the default rooms in the house
        living_room = Room.objects.create(
            house=form.instance,
            **RoomDefinitions.get_room_type_definition(Room.RoomTypeOptions.LIVING_ROOM)
        )
        form.instance.rooms.add(living_room)
        family_den = Room.objects.create(
            house=form.instance,
            **RoomDefinitions.get_room_type_definition(Room.RoomTypeOptions.FAMILY_DEN)
        )
        form.instance.rooms.add(family_den)
        bedroom = Room.objects.create(
            house=form.instance,
            **RoomDefinitions.get_room_type_definition(Room.RoomTypeOptions.BEDROOM)
        )
        form.instance.rooms.add(bedroom)

        return super(HouseCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('house:rooms_list', kwargs={
            'username': self.request.user.username,
            'house_name': self.request.user.house.name
        })


class RoomListView(ExtendedAutoPermissionRequiredMixin, ListView):
    model = Room
    template_name = 'house/room_list.html'
    context_object_name = 'rooms_list'

    def get_queryset(self):
        house = get_object_or_404(House, name=unquote(self.kwargs['house_name']), family__in=[self.request.user])
        return Room.objects.filter(house=house)


class RoomCreateView(ExtendedAutoPermissionRequiredMixin, CreateView):
    model = Room
    fields = ['name', 'cover_image', 'description', 'privacy']

    def form_valid(self, form):
        form.instance.house = get_object_or_404(House, name=unquote(self.kwargs['house_name']),
                                                family__in=[self.request.user])
        form.save()
        return super(RoomCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('house:rooms_list',
                       kwargs={
                           'username': self.request.user.username,
                           'house_name': self.kwargs['house_name']
                       })
