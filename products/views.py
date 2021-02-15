from rest_framework import viewsets
from .models import Product, Bag
from .serializers import ProductSerializer, BagSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

#from .permissions import IsUserBag

from django_filters.rest_framework import DjangoFilterBackend

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BagViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Bag.objects.all()
    serializer_class = BagSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']