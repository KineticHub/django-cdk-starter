from django.urls import path

from justforfam.relations.models import JoinRequest
from justforfam.relations.views import JoinRequestCreateView

app_name = 'relations'
urlpatterns = [
    path('family/', JoinRequestCreateView.as_view(),
        {'type': JoinRequest.JoinTypeOptions.FAMILY},
         name='join_family_request'),
    path('neighbour/', JoinRequestCreateView.as_view(),
         {'type': JoinRequest.JoinTypeOptions.NEIGHBOUR},
         name='join_neighbour_request'),
]
