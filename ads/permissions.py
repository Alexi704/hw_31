from ads.models import Ad
from django.http import Http404
from rest_framework.permissions import BasePermission
from users.models import User


class AdEditPermission(BasePermission):
    """Разрешение на редактирование объявления только для владельцев объявления, админа или модератора."""
    massage = 'only owner or admin (moderator) can edit ads'

    def has_permission(self, request, view):
        if request.user.role in [User.MODERATOR, User.ADMIN]:
            return True

        try:
            ad = Ad.objects.get(pk=view.kwargs['pk'])
        except Ad.DoesNotExist:
            return Http404

        if ad.author_id == request.user.id:
            return True
        return False


