from model_utils.models import TimeStampedModel, UUIDModel
from rules.contrib.models import RulesModelMixin, RulesModelBase


class AbstractBaseModel(UUIDModel, TimeStampedModel, RulesModelMixin, metaclass=RulesModelBase):
    """Represents our base model with common shared fields."""

    class Meta:
        abstract = True
        ordering = ("-created",)
