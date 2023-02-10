from django.apps import AppConfig


# noinspection PyUnresolvedReferences
class GalleryConfig(AppConfig):
    name = 'justforfam.gallery'
    verbose_name = 'Gallery'

    def ready(self):
        import justforfam.gallery.signals
