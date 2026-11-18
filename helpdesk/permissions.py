from rest_framework.permissions import BasePermission
class IsAgentOrAdmin(BasePermission):
    def has_permission(self, req, view):
        return req.user.role in ['admin', 'agent'] and req.user.is_authenticated