from django.urls import include, path

from helpdesk.api.status_ticket import CloseTicketView
from helpdesk.api.ticket import TicketDetailView, TicketListView, TicketView


urlpatterns = [
    path('tickets/', TicketListView.as_view(), name='ticket-list'),
    path('tickets/<str:ticket_number>/', TicketDetailView.as_view(), name='ticket-detail'),
    path('ticket/create/', TicketView.as_view(), name='ticket-create'),
    path('ticket/delete/<str:ticket_number>/', TicketView.as_view(), name='ticket-delete'),
    
    # STATUS UPDATE
    path('ticket/status/close/<str:ticket_number>/', CloseTicketView.as_view(), name='ticket-close'),
    
]