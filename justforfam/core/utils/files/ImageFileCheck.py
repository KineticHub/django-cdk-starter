from django.conf import settings
from django.db.models import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import gettext_lazy as _


class ContentTypeRestrictedFileField(FileField):
    """
    Same as FileField, but you can specify:
        * content_types - list containing allowed content_types. Example: ['application/pdf', 'image/jpeg']
        * max_upload_size - a number indicating the maximum file size allowed for upload.
            2.5MB - 2621440
            5MB - 5242880
            10MB - 10485760
            20MB - 20971520
            50MB - 5242880
            100MB 104857600
            250MB - 214958080
            500MB - 429916160
    """
    def __init__(self, *args, **kwargs):

        self.content_types = kwargs.get("content_types", settings.ALLOWED_IMAGE_TYPES)
        self.max_upload_size = kwargs.get("max_upload_size", settings.MAX_IMAGE_FILE_SIZE)

        super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)

        file = data.file

        try:
            content_type = file.content_type
            if content_type in self.content_types:
                if file._size > self.max_upload_size:
                    raise forms.ValidationError(_('Please keep file size under %s. Current file size is %s')
                                                % (filesizeformat(self.max_upload_size), filesizeformat(file._size)))
            else:
                raise forms.ValidationError(_('File type not supported. Please upload an image.'))
        except AttributeError:
            pass

        return data

    def deconstruct(self):
        name, path, args, kwargs = super(ContentTypeRestrictedFileField, self).deconstruct()
        if 'storage' in list(kwargs.keys()):
            del kwargs['storage']
        if 'upload_to' in list(kwargs.keys()):
            del kwargs['upload_to']
        return name, path, args, kwargs
