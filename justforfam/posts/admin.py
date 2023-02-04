from django.contrib import admin

from justforfam.posts.models import TextPost


@admin.register(TextPost)
class TextPostAdmin(admin.ModelAdmin):
    list_display = ["title", "type"]
    search_fields = ["title"]
    list_filter = ["type"]
