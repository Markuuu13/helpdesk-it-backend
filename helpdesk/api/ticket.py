from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from helpdesk.models import Ticket
from helpdesk.serializers.ticket_serializer import TicketListSerializer, TicketDetailSerializer

class TicketListView(APIView):
    def get(self, request):
        tickets = Ticket.objects.filter(user=request.user)
        serializer = TicketListSerializer(tickets, many=True)
        return Response(serializer.data)