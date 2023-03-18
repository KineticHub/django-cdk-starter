from django.views.generic import ListView, FormView
from rules.contrib.views import AutoPermissionRequiredMixin


class ExtendedAutoPermissionRequiredMixin(AutoPermissionRequiredMixin):
    permission_type_map = [
        (ListView, "view"),
        (FormView, "add"),
        *AutoPermissionRequiredMixin.permission_type_map,
    ]
