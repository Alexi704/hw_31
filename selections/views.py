from selections.permissions import SelectionEditPermission
from selections.serializers import SelectionListSerializer, SelectionDetailSerializer, SelectionSerializer

from selections.models import Selection
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated


class SelectionListView(ListAPIView):
    """Просмотр всех подборок по объявлениям."""
    queryset = Selection.objects.all()
    serializer_class = SelectionListSerializer


class SelectionDetailView(RetrieveAPIView):
    """Просмотр подбороки по ее id."""
    queryset = Selection.objects.all()
    serializer_class = SelectionDetailSerializer


class SelectionCreateView(CreateAPIView):
    """Создание подборки (только для зарегистрированных пользователей)."""
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated]


class SelectionUpdateView(UpdateAPIView):
    """Обновление подборки по ее id. Только для владельцев подборки."""
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated, SelectionEditPermission]


class SelectionDeleteView(DestroyAPIView):
    """Удаление подборки по ее id. Только для создателя подборки."""
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated, SelectionEditPermission]
