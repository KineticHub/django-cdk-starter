from django.db import models
from django.db.models import CASCADE

from justforfam.core.models.base import AbstractBaseModel
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

    class RoomPrivacyOptions(models.TextChoices):
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
    privacy = models.CharField(
        max_length=255,
        choices=RoomPrivacyOptions.choices,
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


class PrivateRoom(AbstractBaseModel):

    class PrivateRoomPrivacyOptions(models.TextChoices):
        PRIVATE = "private", "Private"
        PERSONAL_GUESTS = "personal-guests", "Personal Guests"

    house = models.ForeignKey(
        House,
        related_name='private_rooms',
        on_delete=CASCADE
    )
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    privacy = models.CharField(
        max_length=255,
        choices=PrivateRoomPrivacyOptions.choices,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.name
