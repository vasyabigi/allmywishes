from rest_framework import permissions


class IsWishOwnerPermission(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        """
        Check if request user is owner of current wish.

        """
        return obj.account == request.user
