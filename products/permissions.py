from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
#TODO: Tem q arrumar isso, atualmente nao funciona e eu nao sei bem o pq
# muito menos como arrumar
class IsUserBag(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            obj.user == request.user or
            request.user and request.user.is_staff
        )