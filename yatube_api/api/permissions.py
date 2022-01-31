from rest_framework import permissions


class ChangeMadeOwner(permissions.BasePermission):

    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.method in permissions.SAFE_METHODS:
                return True
            return obj.author == request.user
        return False
