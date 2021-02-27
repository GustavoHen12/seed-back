from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny

from .models import Product, Bag
from .serializers import ProductSerializer, BagSerializer

#from .permissions import IsUserBag

from django_filters.rest_framework import DjangoFilterBackend

import logging
logger = logging.getLogger(__name__)

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BagViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Bag.objects.all()
    serializer_class = BagSerializer
    
    def get_queryset(self):
        queryset = Bag.objects.filter(user=self.request.user)
        return queryset

    def create(self, request):
        data = Bag.objects.all()
        serializer = BagSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.validated_data
            product = serializer.validated_data["product"]
            filter = Bag.objects.filter(user=self.request.user, product=product.id)
            if len(filter) > 0 :
                for item in filter:
                    item.quantity = serializer.data["quantity"]
                    item.save()
            else:
                serializer.save()    
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        data = Bag.objects.all()
        serializer = BagSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.validated_data
            product = serializer.data["product"]
            filter = Bag.objects.filter(user=self.request.user, product=product["id"])
            if len(filter) > 0 :
                for item in filter:
                    item.delete()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        