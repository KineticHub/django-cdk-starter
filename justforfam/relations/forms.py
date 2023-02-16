import logging

from django import forms

from justforfam.core.utils.mixins import AddRequestToFormMixin
from justforfam.house.models import House
from justforfam.relations.models import JoinRequest


class JoinRequestForm(AddRequestToFormMixin, forms.ModelForm):
    house_id = forms.CharField(required=True, max_length=64)

    class Meta:
        model = JoinRequest
        fields = ['house_id']

    def clean(self):
        if not House.objects.filter(id=self.cleaned_data['house_id']).exists():
            raise forms.ValidationError('Home not found.')
        house = House.objects.get(id=self.cleaned_data['house_id'])
        if JoinRequest.objects.filter(requester=self.request.user, house=house).exists():
            raise forms.ValidationError('Request already exists to join this home.')
