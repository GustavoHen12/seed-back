from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from kit.permissions import IsAdminOrReadOnly

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer