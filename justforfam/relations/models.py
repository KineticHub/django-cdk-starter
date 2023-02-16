from django.db import models
from django.db.models import CASCADE, SET_NULL

from justforfam.core.models.base import AbstractBaseModel
from justforfam.house.models import House
from justforfam.relations import rules
from justforfam.users.models import User


class JoinRequest(AbstractBaseModel):

    class JoinTypeOptions(models.TextChoices):
        FAMILY = "family", "Family"
        NEIGHBOUR = "neighbour", "Neighbour"

    requester = models.ForeignKey(
        User,
        on_delete=CASCADE,
        related_name='join_requests'
    )
    house = models.ForeignKey(
        House,
        on_delete=CASCADE,
        related_name='join_requests'
    )
    type = models.CharField(
        max_length=255,
        choices=JoinTypeOptions.choices,
        default=JoinTypeOptions.NEIGHBOUR
    )
    approval = models.BooleanField(default=None, null=True)
    approval_by = models.ForeignKey(
        User,
        on_delete=SET_NULL,
        null=True,
        blank=True,
        related_name='approval_requests'
    )

    class Meta:
        rules_permissions = {
            "add": rules.can_add_request,
            "change": rules.can_edit_request,
            "delete": rules.can_delete_request,
            "view": rules.can_view_request,
            # "respond": rules.can_respond_request
        }
