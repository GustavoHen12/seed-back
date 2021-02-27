from rest_framework import serializers
from .models import Project, Kit, Kit_product
from products.serializers import ProductSerializer

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class KitSerializer(serializers.HyperlinkedModelSerializer):
    # project = serializers.PrimaryKeyRelatedField(
    #     many=False,
    #     read_only=True
    # )
    project = ProjectSerializer(
        many=False,
        read_only=True
    )
    class Meta:
        model = Kit
        fields = ('id', 'name', 'project', 'description', 'img', 'imgUrl', 'goal')

class KitProductSerializer(serializers.HyperlinkedModelSerializer):
    kit = KitSerializer(
        many=False,
        read_only=True
    )
    product = ProductSerializer(
        many=False,
        read_only=True
    )
    class Meta:
        model = Kit_product
        fields = '__all__'