from selections.models import Selection
from django.http import Http404
from rest_framework.permissions import BasePermission
from users.models import User


class SelectionEditPermission(BasePermission):
    """Разрешение на редактирование подборки объявлений только для ее владельца."""
    massage = 'You can only edit your own selections'

    def has_permission(self, request, view):
        try:
            selection = Selection.objects.get(pk=view.kwargs['pk'])
        except Selection.DoesNotExist:
            raise Http404

        if selection.owner_id == request.user.id:
            return True
        return False
