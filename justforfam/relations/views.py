from django.contrib import messages
from django.views.generic import CreateView

from justforfam.core.utils.mixins import PassRequestToFormViewMixin
from justforfam.core.utils.permissions import ExtendedAutoPermissionRequiredMixin
from justforfam.house.models import House
from justforfam.relations.forms import JoinRequestForm
from justforfam.relations.models import JoinRequest


class JoinRequestCreateView(PassRequestToFormViewMixin, ExtendedAutoPermissionRequiredMixin, CreateView):
    model = JoinRequest
    form_class = JoinRequestForm

    def form_valid(self, form):
        # we can do this safely because the form class checks the existence
        house = House.objects.get(id=form.cleaned_data['house_id'])

        # fill in the instance with the actual values we did not want the user adding
        form.instance.requester = self.request.user
        form.instance.house = house
        form.instance.type = self.kwargs['type']

        # let it fly
        return super(JoinRequestCreateView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "Request to join home sent.")
        return self.request.META.get('HTTP_REFERER')
