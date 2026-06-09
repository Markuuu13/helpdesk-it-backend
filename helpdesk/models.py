from django.db import models

from helpdesk_auth.configs.custom_managers import ActiveManager, AllManager
from helpdesk_auth.mixins import SoftDeleteMixin
from helpdesk_auth.models import Users

# Create your models here.
class Ticket(SoftDeleteMixin):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed')
    ]
    ticket_number = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='tickets')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tickets')
    asset = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    
    objects = ActiveManager()
    all_objects = AllManager()
    
    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'

    def __str__(self):
        return self.title