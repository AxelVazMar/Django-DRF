# Primero importaciones nativas
from rest_framework import generics

# Segundo las importaciones propias
from apps.products.models import MeasureUnit, CategoryProduct, Indicator
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer, IndicatorSerializer

class MeasureUnitListAPIView(generics.ListAPIView):
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        """
        Consulta/Queryset para convertir en JSON todos los objetos del modelo MeasureUnit
        """
        # Este queryset filtra por los objetos que su estado es True, osea que están activos
        return MeasureUnit.objects.filter(state=True)

class CategoryProductListAPIView(generics.ListAPIView):
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        """
        Queryset para convertir a JSON todos los objetos del modelo CategoryProduct
        """
        return CategoryProduct.objects.filter(state=True)
    
class IndicatorListAPIView(generics.ListAPIView):
    serializer_class = IndicatorSerializer

    def get_queryset(self):
        """
        Queryset para convertir a JSON todos los objetos del modelo Indicator
        """
        return Indicator.objects.filter(state=True)