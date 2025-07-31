from rest_framework import generics, status
from rest_framework.response import Response

from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.product_serializer import ProductSerializer

class ProductListAPIView(GeneralListAPIView):
    serializer_class = ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def post(self, request):
        """
        Sobreescribiendo la función "POST" de "CreateAPIView" para
        personalizarla y que haga lo que queramos
        """
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Producto creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        Esta función está haciendo un override a la función get_queryset() de los serializers
        Esto nos permite ver los objetos de products cuando le pasamos un ID en especifico
        """
        
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
class ProductDestroyAPIView(generics.DestroyAPIView):
    """
    Este método es una eliminación directa en la base de datos y no se usa frecuentemente
    La más usada es la eliminación lógica, y eso lo hacemos con un override a la función delete
    """
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    def delete(self, request, pk=None):
        """
        Aquí estamos haciendo un override a la función delete para solo hacer un borrado lógico
        y no hacer un borrado directo a la bdd
        """
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message': 'Prodcuto eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe un producto con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

