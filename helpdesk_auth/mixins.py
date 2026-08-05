from django.utils import timezone
from django.db import models

from helpdesk_auth.models import Users

class SoftDeleteMixin(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        abstract = True
        
    def delete(self, *args, **kwargs):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.status = 'deleted'
        self.save()
    
    def hard_delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        
    def restore(self, *args, **kwargs):
        self.deleted_at = None
        self.is_deleted = False
        self.save()

class UpdateMixin(models.Model):
    updated_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_%(class)s_set')
    
    class Meta:
        abstract = True
    
    def in_progress_status(self, *args, **kwargs):
        self.status = 'in_progress'
        self.save()
    
    def resolved_status(self, *args, **kwargs):
            self.status = 'resolved'
            self.save()
    
    def closed_status(self, *args, **kwargs):
            self.status = 'closed'
            self.save()