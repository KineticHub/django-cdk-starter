from django.views.generic import ListView
from rules.contrib.views import AutoPermissionRequiredMixin


class ExtendedAutoPermissionRequiredMixin(AutoPermissionRequiredMixin):
    permission_type_map = [
        (ListView, "view"),
        *AutoPermissionRequiredMixin.permission_type_map,
    ]
