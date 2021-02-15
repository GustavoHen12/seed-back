from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)
router.register(r'bag', views.BagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]