from rest_framework import permissions

class IsProjectOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user making the request is the owner of the project
        return obj.company == request.user