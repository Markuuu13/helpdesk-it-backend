
from helpdesk.models import Ticket
from rest_framework import serializers
from django.db import transaction
from django.utils import timezone
import uuid


class TicketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            'ticket_number',
            'title',
            'created_by',
            'created_at',
            'asset',
            'status'
        ]

class TicketDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            'title',
            'description',
            'asset',
        ]
        
    def create(self, validated_data):
        # Generate a unique ticket number
        validated_data['ticket_number'] = self.generate_ticket_number()
        return super().create(validated_data)

    @staticmethod
    def generate_ticket_number():
        year = timezone.now().year
        prefix = f"TCKT{year}"
        
        while True:
            ticket = f"{prefix}{uuid.uuid4().hex[:8].upper()}"
            if not Ticket.objects.filter(ticket_number=ticket).exists():
                return ticket