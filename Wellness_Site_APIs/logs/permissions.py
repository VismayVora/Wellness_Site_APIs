from rest_framework.permissions import BasePermission, SAFE_METHODS

class EditLogPermission(BasePermission):
    message = "Only viewing users logs is allowed."

    def has_permission(self, request, view):
        
        if request.method in SAFE_METHODS:
            return True
    
    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.owner == request.user
