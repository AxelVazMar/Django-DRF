# Primero importaciones nativas
from rest_framework import viewsets
from rest_framework.response import Response

# Segundo las importaciones propias
from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer, IndicatorSerializer
from apps.products.models import MeasureUnit

class MeasureUnitViewSet(viewsets.GenericViewSet):
    serializer_class = MeasureUnitSerializer
    model = MeasureUnit
    
    def get_queryset(self):
        return self.get_serializer().Meta.objects.filter(state=True)
    

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)

class CategoryProductViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer
    
class IndicatorViewSet(viewsets.ModelViewSet):
    serializer_class = IndicatorSerializer
