from rest_framework import serializers

from apps.products.models import Product
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer

class ProductSerializer(serializers.ModelSerializer):

    """ 
    La forma de abajo es una manera de hacer que se muestre la información de de otros serializadores dentro de un serializador 
    Pero esta forma retornará toda la información del serializador, por lo que puede que haya información que no quieras que se muestre    
    """
    # measure_unit = MeasureUnitSerializer() # <== las variables tienen que ser declaradas iguales que en el modelo
    # category_product = CategoryProductSerializer() # <== las variables tienen que ser declaradas iguales que en el modelo

    """ Esta manera accede al método __str__() de la clase de los serializadores y muestra lo que se retorna ahí """
    # measure_unit = serializers.StringRelatedField()
    # category_product = serializers.StringRelatedField()

    class Meta:
        model = Product
        exclude = ('created_date', 'modified_date', 'deleted_day')
    
    def to_representation(self, instance):
        """
        Esta forma es para hacer override del método to represetation  y aquí podemos manipular la data sin tener que modificar el serializador principal
        """
        return {
            'id': instance.id,
            'description': instance.description,
            'image': instance.image if instance.image != '' else 'No image', # <== esta es una ventaja que da este método, podemos agregar validaciones
            'measure_unit': instance.measure_unit.description,
            'category_product': instance.category_product.description,

        }