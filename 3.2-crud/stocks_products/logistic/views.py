from rest_framework.viewsets import ModelViewSet

from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer
import django_filters


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
