from django.db import models

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class AllManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()