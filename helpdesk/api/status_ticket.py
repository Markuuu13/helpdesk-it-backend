from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from helpdesk.models import Ticket
from helpdesk.serializers.ticket_serializer import TicketDetailSerializer

class CloseTicketView(APIView):
    permission_classes = [IsAuthenticated]
    
    def patch(self, request, ticket_number):
        try:
            ticket = Ticket.objects.get(ticket_number=ticket_number)
        except Ticket.DoesNotExist:
            return Response({"message": "Ticket not found."}, status=status.HTTP_404_NOT_FOUND)
        
        user = request.user
        
        serializer = TicketDetailSerializer(ticket, many=False)
        
        if user.role == 'admin' or user.role == 'agent':
            ticket.closed_status()
            return Response({"message": "Ticket closed.", "data": serializer.data}, status=status.HTTP_200_OK)
        
        return Response({"message": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)
        
        