from rest_framework import permissions


# To authenticate users and ensure that only theowner of a post can update or delete an existing post
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
