from rest_framework import serializers
from .models import Product, Bag

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    outfitter = serializers.StringRelatedField(
        many=False,
        read_only=True
    )
    class Meta:
        model = Product
        fields = '__all__'

class BagSerializer(serializers.HyperlinkedModelSerializer):
    kit = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True
    )
    product = ProductSerializer(
        many=False,
        read_only=True
    )
    user = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True
    ) 
    class Meta:
        model = Bag
        fields = '__all__'