from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, SET_NULL
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from justforfam.core.models.base import AbstractBaseModel


class User(AbstractUser, AbstractBaseModel):
    """
    Default custom user model for JustForFam.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    name = CharField(
        _("Name of User"),
        blank=True,
        max_length=255
    )
    house = models.ForeignKey(
        'house.House',
        related_name='family',
        on_delete=SET_NULL,
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
