from apps.products.models import CategoryProduct, MeasureUnit, Indicator

from rest_framework import serializers

"""
Serializadores generales para los campos generales de la BDD de la app "Productos"
"""

class MeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        exclude = ('state',)

class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        exclude = ('state',)

class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        exclude = ('state',)