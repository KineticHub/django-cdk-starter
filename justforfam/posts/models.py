from django.db import models
from django.db.models import SET_NULL, CASCADE
from tinymce import models as tinymce_models

from justforfam.core.models.base import AbstractBaseModel
from justforfam.core.utils.files.FileUploadTo import FileUploadTo
from justforfam.core.utils.files.ImageFileCheck import ContentTypeRestrictedFileField
from justforfam.house.models import Room
from justforfam.posts import rules
from justforfam.users.models import User


class Post(AbstractBaseModel):
    """
    Base model for all Post models
    """

    class PostTypeOptions(models.TextChoices):
        TEXT = "text", "Text"
        RECIPE = "recipe", "Recipe"

    # ======================================
    # Fields
    # ======================================
    author = models.ForeignKey(
        User,
        on_delete=CASCADE,
        default=0
    )
    title = models.CharField(
        max_length=255,
        default="Untitled"
    )
    subtitle = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    banner_image = ContentTypeRestrictedFileField(
        upload_to=FileUploadTo("posts/banners/"),
        null=True,
        blank=True
    )
    room = models.ForeignKey(
        Room,
        related_name='posts',
        on_delete=SET_NULL,
        null=True
    )
    type = models.CharField(
        max_length=255,
        choices=PostTypeOptions.choices,
        default=PostTypeOptions.TEXT
    )
    content = tinymce_models.HTMLField()

    class Meta:
        rules_permissions = {
            "add": rules.can_add_post,
            "change": rules.can_edit_post,
            "delete": rules.can_delete_post,
            "view": rules.can_view_post,
        }

    def __str__(self):
        return self.title
