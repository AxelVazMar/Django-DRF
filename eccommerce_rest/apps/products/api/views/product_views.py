from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.product_serializer import ProductSerializer

class ProductListAPIView(GeneralListAPIView):
    serializer_class = ProductSerializer
    