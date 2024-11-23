from rest_framework import permissions

class IsColecionador(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.colecionador == request.user
