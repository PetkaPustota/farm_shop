from rest_framework.permissions import BasePermission


class ProfileUserPermission(BasePermission):
    message = "This Profile for this user not allowed."

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user_id:
            return True
        return False
