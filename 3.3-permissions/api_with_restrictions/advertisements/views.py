from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement
from .serializers import AdvertisementSerializer
from .permissions import IsOwnerOrReadOnly

class AdvertisementViewSet(ModelViewSet):
    qweryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        elif self.action in ["update", "partial_update", 'destroy']:
            return[IsOwnerOrReadOnly]
        return []
