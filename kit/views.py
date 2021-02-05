from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Project, Kit, Kit_product
from .serializers import ProjectSerializer, KitSerializer, KitProductSerializer

from rest_framework import permissions
from .permissions import IsAdminOrReadOnly

class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
class KitViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Kit.objects.all()
    serializer_class = KitSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['project']

class KitProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Kit_product.objects.all()
    serializer_class = KitProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['kit']