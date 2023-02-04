from django.contrib import admin

from justforfam.house.models import House, Room


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = []


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = []
