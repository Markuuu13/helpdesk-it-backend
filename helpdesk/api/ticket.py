from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from helpdesk.models import Ticket
from rest_framework.permissions import IsAuthenticated
from helpdesk.serializers.ticket_serializer import TicketListSerializer, TicketDetailSerializer

class TicketListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        tickets = Ticket.objects.filter(assigned_to=request.user)
        serializer = TicketListSerializer(tickets, many=True)
        return Response(serializer.data)
