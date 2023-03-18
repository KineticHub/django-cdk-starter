from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView

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


class JoinRequestListView(ExtendedAutoPermissionRequiredMixin, ListView):
    model = JoinRequest
    template_name = 'relations/joinrequest_list.html'
    context_object_name = 'requests_list'

    def get(self, request, *args, **kwargs):

        approval_id = request.GET.get('approvalId', None)
        approval_decision = request.GET.get('approvalDecision', None)
        is_approved = approval_decision in ['approved', 'approve']

        if approval_id is not None and approval_decision is not None:
            join_request = get_object_or_404(JoinRequest, id=approval_id)

            if join_request.house.family.filter(id=request.user.id).exists():
                join_request.approval_by = request.user
                join_request.approval = is_approved
                join_request.save()

                if is_approved:
                    join_request.requester.house = join_request.house
                    join_request.requester.save()

            return redirect(reverse('relations:join_request_list', kwargs={'username': request.user.username}))

        return super(JoinRequestListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return {
            "outgoing": {
                "family": JoinRequest.objects
                .filter(requester=self.request.user, type=JoinRequest.JoinTypeOptions.FAMILY)
                .exclude(approval_by__isnull=False),

                "neighbour": JoinRequest.objects
                .filter(requester=self.request.user, type=JoinRequest.JoinTypeOptions.NEIGHBOUR)
                .exclude(approval_by__isnull=False)

            },
            "incoming": {
                "family": JoinRequest.objects
                .filter(house=self.request.user.house, type=JoinRequest.JoinTypeOptions.FAMILY)
                .exclude(approval_by__isnull=False),
                "neighbour": JoinRequest.objects
                .filter(house=self.request.user.house, type=JoinRequest.JoinTypeOptions.NEIGHBOUR)
                .exclude(approval_by__isnull=False),
            }
        }
