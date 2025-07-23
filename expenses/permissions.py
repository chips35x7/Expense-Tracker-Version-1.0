from rest_framework import permissions

class IsOwnerOrRestrictAccess(permissions.BasePermission):
    """The permissions class to make sure that only the user who created expenses can view them"""
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user