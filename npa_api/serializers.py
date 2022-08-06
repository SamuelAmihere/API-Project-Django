"""
Describing the process of going from a python object to a json object
""" 
from rest_framework import serializers
from .models import MarketCategory,Player,Product


class MarketCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketCategory
        fields = ['id','name','description']


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id','name','market_type']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','description']