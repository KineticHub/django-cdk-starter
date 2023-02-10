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
    family = models.ManyToManyField(
        User,
        related_name='family_houses'
    )
    family_guests = models.ManyToManyField(
        User,
        related_name='guest_houses',
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


class RoomBase(AbstractBaseModel):
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

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Room(RoomBase):

    class RoomPrivacyOptions(models.TextChoices):
        FAMILY = "family", "Family"
        FAMILY_GUESTS = "family-guests", "Family Guests"
        PUBLIC = "public", "Public"

    house = models.ForeignKey(
        House,
        related_name='rooms',
        on_delete=CASCADE
    )
    privacy = models.CharField(
        max_length=255,
        choices=RoomPrivacyOptions.choices,
        null=False,
        blank=False
    )

    class Meta(RoomBase.Meta):
        rules_permissions = {
            "add": rules.can_add_room,
            "change": rules.can_edit_room,
            "delete": rules.can_delete_room,
            "view": rules.can_view_room,
        }


class PrivateRoom(RoomBase):

    class PrivateRoomPrivacyOptions(models.TextChoices):
        PRIVATE = "private", "Private"
        PERSONAL_GUESTS = "personal-guests", "Personal Guests"

    house = models.ForeignKey(
        House,
        related_name='private_rooms',
        on_delete=CASCADE
    )
    privacy = models.CharField(
        max_length=255,
        choices=PrivateRoomPrivacyOptions.choices,
        null=False,
        blank=False
    )
