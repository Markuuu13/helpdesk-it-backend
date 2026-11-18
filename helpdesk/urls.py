from django.urls import include, path

from helpdesk.api.status_ticket import CloseTicketView, ClosedTicketView, InProgressTicketView, ResolvedTicketView
from helpdesk.api.ticket import TicketDetailView, TicketListView, TicketRecentView, TicketView


urlpatterns = [
    path('tickets/', TicketListView.as_view(), name='ticket-list'),
    path('tickets/<str:ticket_number>/', TicketDetailView.as_view(), name='ticket-detail'),
    path('ticket/create/', TicketView.as_view(), name='ticket-create'),
    path('ticket/delete/<str:ticket_number>/', TicketView.as_view(), name='ticket-delete'),
    path('ticket/recent/', TicketRecentView.as_view(), name='ticket-recent'),
    
    # STATUS UPDATE
    path('ticket/status/close/<str:ticket_number>/', CloseTicketView.as_view(), name='ticket-close'),
    path('ticket/status/in_progress/<str:ticket_number>/', InProgressTicketView.as_view(), name='ticket-in-progress'),
    path('ticket/status/resolved/<str:ticket_number>/', ResolvedTicketView.as_view(), name='ticket-resolved'),
]