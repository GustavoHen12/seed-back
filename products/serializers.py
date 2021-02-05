from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    outfitter = serializers.StringRelatedField(
        many=False,
        read_only=True
    )
    class Meta:
        model = Product
        fields = '__all__'