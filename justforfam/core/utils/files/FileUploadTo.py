import os
from uuid import uuid4

from django.db import models
from django.utils.deconstruct import deconstructible


@deconstructible
class FileUploadTo:
    """
    Use the callable class pattern so we can pass in the path we want to store the files.

    Since all components are serializable, we can add the deconstructible for Django migrations.
    https://docs.djangoproject.com/en/4.1/topics/migrations/#adding-a-deconstruct-method
    """

    def __init__(self, file_path: str):
        self._file_path = os.path.join(file_path, "")  # Adds trailing slash if missing.

    def __call__(self, instance: models.Model, filename: str) -> str:
        _, filename_ext = os.path.splitext(filename)
        filename = "{}{}".format(str(uuid4()), filename_ext)
        return os.path.join(self._file_path, filename)
