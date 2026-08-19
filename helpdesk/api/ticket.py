from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from helpdesk.models import Ticket
from rest_framework.permissions import IsAuthenticated
from helpdesk.serializers.ticket_serializer import TicketCreateSerializer, TicketListSerializer, TicketDetailSerializer


class TicketListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        role = request.user.role
        if role == 'admin' or role == 'agent':
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

        if (request.user.role != 'admin' and ticket.created_by != request.user):
            return Response({"message": "You do not have permission to view this ticket."}, status=status.HTTP_403_FORBIDDEN)

        serializer = TicketDetailSerializer(ticket, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TicketView(APIView):
    permission_classes = [IsAuthenticated]

    # Create Ticket
    def post(self, request):
        serializer = TicketCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete Ticket
    def delete(self, request, ticket_number):
        try:
            ticket = Ticket.objects.get(ticket_number=ticket_number)
        except Ticket.DoesNotExist:
            return Response({"message": "Ticket not found."}, status=status.HTTP_404_NOT_FOUND)

        user = request.user

        if user.role == 'admin' or user.role == 'agent':
            ticket.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response({"message": "You do not have permission to delete this ticket."}, status=status.HTTP_403_FORBIDDEN)
           

        
