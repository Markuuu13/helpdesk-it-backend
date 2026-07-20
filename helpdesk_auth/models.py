from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('agent', 'Agent'),
        ('admin', 'Admin'),
    ]
    name = models.CharField(max_length=200, blank=True, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def is_agent(self):
        return self.role == 'agent'
    
    def is_admin(self):
        return self.role == 'admin'
    
    def __str__(self):
        return self.name