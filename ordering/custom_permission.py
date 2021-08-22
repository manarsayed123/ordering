from rest_framework.permissions import BasePermission


class IsNormalUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and not request.user.is_staff)
