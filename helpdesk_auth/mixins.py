from django.utils import timezone
from django.db import models

class SoftDeleteMixin(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        abstract = True
        
    def delete(self, *args, **kwargs):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()
    
    def hard_delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        
    def restore(self, *args, **kwargs):
        self.deleted_at = None
        self.is_deleted = False
        self.save()