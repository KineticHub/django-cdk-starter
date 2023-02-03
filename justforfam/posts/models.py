from django.db import models

from justforfam.core.models.base import AbstractBaseModel
from justforfam.users.models import User


# from django.db.models import CharField
# from django.urls import reverse
# from django.utils.translation import gettext_lazy as _
#
#
class PostBase(AbstractBaseModel):
    """
    Base model for all Post models
    """

    # ======================================
    # Choices
    # ======================================
    class PostType(models.TextChoices):
        TEXT = "text", "Text"
        RECIPE = "recipe", "Recipe"

    class PostLocation(models.TextChoices):
        BEDROOM = "bedroom", "Bedroom"
        KITCHEN = "kitchen", "Kitchen"

    # ======================================
    # Fields
    # ======================================
    user = models.ForeignKey(
        User, related_name="posts", on_delete=models.CASCADE
    )
    type = models.CharField(
        max_length=255,
        choices=PostType.choices,
        default=PostType.TEXT,
        null=True,
        blank=True,
    )
    location = models.CharField(
        max_length=255,
        choices=PostLocation.choices,
        default=PostLocation.BEDROOM,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class TextPost(PostBase):
    """
    Simple text based post
    """
    # cover_image = models.FileField(
    #     upload_to=ModelUploadTo("posts/cover/"), null=True, blank=True
    # )
    content = models.TextField(
        blank=True, null=True
    )
#
#     #: First and last name do not cover name patterns around the globe
#     name = CharField(_("Name of User"), blank=True, max_length=255)
#     first_name = None  # type: ignore
#     last_name = None  # type: ignore
#
#     def get_absolute_url(self):
#         """Get url for user's detail view.
#
#         Returns:
#             str: URL for user detail.
#
#         """
#         return reverse("users:detail", kwargs={"username": self.username})
