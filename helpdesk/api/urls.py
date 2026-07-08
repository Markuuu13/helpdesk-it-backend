

from django.urls import include, path

from helpdesk.api.ticket import TicketListView


urlpatterns = [
    path('tickets/', TicketListView.as_view(), name='ticket-list'),
]