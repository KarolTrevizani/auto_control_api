from rest_framework import serializers

from .models import *


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'created_at')
        
        
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'name', 'created_at')

    
class VehicleSerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(source='type.name', read_only=True)
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    owner_name = serializers.CharField(source='owner.name', read_only=True)
    
    class Meta:
        model = Vehicle
        fields = ('id', 'name', 'owner', 'owner_name', 'description', 'type', 'type_name', 'brand', 'brand_name', 'created_at')