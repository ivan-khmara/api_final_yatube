from rest_framework import permissions


class ChangeMadeOwner(permissions.BasePermission):

    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        if not request.user:
            return False
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
