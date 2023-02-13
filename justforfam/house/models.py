from django.db import models
from django.db.models import CASCADE

from justforfam.core.models.base import AbstractBaseModel
from justforfam.core.utils.files.FileUploadTo import FileUploadTo
from justforfam.core.utils.files.ImageFileCheck import ContentTypeRestrictedFileField
from justforfam.house import rules
from justforfam.users.models import User


class House(AbstractBaseModel):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    neighbours = models.ManyToManyField(
        User,
        related_name='neighbours',
        null=True,
        blank=True
    )
    cover_image = ContentTypeRestrictedFileField(
        upload_to=FileUploadTo("rooms/covers/"),
        null=True,
        blank=True
    )

    class Meta:
        rules_permissions = {
            "add": rules.can_add_house,
            "change": rules.can_edit_house,
            "delete": rules.can_delete_house,
            "view": rules.can_view_house,
        }

    def __str__(self):
        return self.name


class Room(AbstractBaseModel):

    class RoomTypeOptions(models.TextChoices):
        LIVING_ROOM = "living-room", "Living Room"
        FAMILY_DEN = "family-den", "Family Den"
        BEDROOM = "bedroom", "Bedroom"

    class RoomPrivacyOptions(models.TextChoices):
        PRIVATE = "private", "Private"
        PERSONAL_GUESTS = "personal-guests", "Personal Guests"
        FAMILY = "family", "Family"
        FAMILY_GUESTS = "family-guests", "Family Guests"
        PUBLIC = "public", "Public"

    house = models.ForeignKey(
        House,
        related_name='rooms',
        on_delete=CASCADE
    )
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    cover_image = ContentTypeRestrictedFileField(
        upload_to=FileUploadTo("rooms/covers/"),
        null=True,
        blank=True
    )
    privacy = models.CharField(
        max_length=255,
        choices=RoomPrivacyOptions.choices,
        null=False,
        blank=False
    )
    type = models.CharField(
        max_length=255,
        choices=RoomTypeOptions.choices,
        default=RoomTypeOptions.LIVING_ROOM,
        null=False,
        blank=False
    )

    class Meta:
        rules_permissions = {
            "add": rules.can_add_room,
            "change": rules.can_edit_room,
            "delete": rules.can_delete_room,
            "view": rules.can_view_room,
        }

    def __str__(self):
        return self.name

    @property
    def get_default_cover_image_static_file_path(self):
        if self.type == Room.RoomTypeOptions.LIVING_ROOM:
            return 'images/rooms/living-room-2-crop.png'
        if self.type == Room.RoomTypeOptions.FAMILY_DEN:
            return 'images/rooms/home-office-2.png'
        if self.type == Room.RoomTypeOptions.BEDROOM:
            return 'images/rooms/bedroom-2.png'
