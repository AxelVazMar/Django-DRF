from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.product_serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    Creando nuestro primer ViewSet
    para que funcione debemos enlazarlo a un "ROUTER"
    """
    serializer_class = ProductSerializer
    #queryset = ProductSerializer.Meta.model.objects.filter(state=True)

    def get_queryset(self, pk=None):
        """
        Esta función hacer el override de la función get_queryset() de los ViewSets
        Aquí estamos obteniendo todos los objetos del serialiazer de serialiazer_class=ProductSerializer
        """
        if pk is None:
            # Si no se le pasa un pk/id devuelve todo los objetos del serializador
            return self.get_serializer().Meta.model.objects.filter(state=True)
        
        # Si se le pasa un pk/id regresa el primer resultado ejemplo pk = 4 entonces devolverá el objeto con id = 4
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()
    
    def list(self, request):
        product_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        """
        Override del método CREATE (post) de los ViewSets
        """
        print("Hola desde create")
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':'producto creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)

            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response({'error':'no existe un producto con esos datos'}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        """
        Aquí estamos haciendo un override a la función delete para solo hacer un borrado lógico y 
        no hacer un borrado directo a la bdd
        """
        product = self.get_queryset().filter(id = pk).first()

        if product:
            product.state = False
            product.save()
            return Response({'message':'producto eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'no existe producto con esos datos'}, status=status.HTTP_400_BAD_REQUEST)
    