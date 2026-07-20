from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from helpdesk.models import Ticket
from rest_framework.permissions import IsAuthenticated
from helpdesk.serializers.ticket_serializer import TicketListSerializer, TicketDetailSerializer

class TicketListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):

        role = request.user.role
        if role == 'admin':
            tickets = Ticket.objects.filter(assigned_to=request.user)
            serializer = TicketListSerializer(tickets, many=True)
            return Response(serializer.data)

        return Response({"message": "You do not have permission to view tickets."}, status=status.HTTP_403_FORBIDDEN)

class TicketDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, ticket_number):
        try:
            ticket = Ticket.objects.get(ticket_number=ticket_number)
        except Ticket.DoesNotExist:
            return Response({"message": "Ticket not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if(request.user.role != 'admin' and ticket.created_by != request.user):    
            return Response({"message": "You do not have permission to view this ticket."}, status=status.HTTP_403_FORBIDDEN)
    
        serializer = TicketDetailSerializer(ticket, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)