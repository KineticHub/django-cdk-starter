from django.contrib import admin

from justforfam.relations.models import JoinRequest


@admin.register(JoinRequest)
class JoinRequestAdmin(admin.ModelAdmin):
    list_display = ["requester", "house"]
    search_fields = ["requester", "house"]
    list_filter = ["house"]
