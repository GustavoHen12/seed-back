from rest_framework import serializers
from .models import Product, Bag
from kit.models import Kit
from django.contrib.auth.models import  User

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    outfitter = serializers.StringRelatedField(
        many=False,
        read_only=True
    )
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'img', 'imgUrl', 'price', 'outfitter')

class BagSerializer(serializers.HyperlinkedModelSerializer):
    kit = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Kit.objects.all(),
    )
    product = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Product.objects.all(),
    ) 
    user = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=User.objects.all(),
    ) 
    class Meta:
        model = Bag
        fields = ('quantity', 'kit', 'product', 'user')

    def to_representation(self, instance):
        self.fields['product'] =  ProductSerializer(read_only=True)
        return super(BagSerializer, self).to_representation(instance)
