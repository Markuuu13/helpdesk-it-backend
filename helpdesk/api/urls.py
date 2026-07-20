

from django.urls import include, path

from helpdesk.api.ticket import TicketDetailView, TicketListView


urlpatterns = [
    path('tickets/', TicketListView.as_view(), name='ticket-list'),
    path('tickets/<int:ticket_number>/', TicketDetailView.as_view(), name='ticket-detail'),
]