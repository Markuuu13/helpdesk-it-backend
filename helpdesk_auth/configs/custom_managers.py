from django.db import models
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

class PublicAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class AllManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()