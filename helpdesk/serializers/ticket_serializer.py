
from helpdesk.models import Ticket
from rest_framework import serializers


class TicketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            'ticket_number',
            'title',
            'description',
            'created_by',
            'created_at',
            'updated_at',
            'asset',
            'status'
        ]

class TicketDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
