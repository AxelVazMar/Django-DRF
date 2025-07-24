from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer, TestUserSerializer


    # def get(self, request): # Creando la petición HTTP 'GET'
        
    #     users = User.objects.all() # Haciendo consulta SQL 'FROM users SELECT *'
    #     users_serializers = UserSerializer(users, many=True) # Diciendole a DJANGO qué, debe listar. El 'many=True' es para decirle a DJANGO que debe listar todos los resultados de la consulta SQL
        
    #     return Response(users_serializers.data, status=status.HTTP_200_OK) # '.data' es para retornar la información serializada y convertida a JSON

@api_view(['GET', 'POST']) # Decorador @api_view para crear las peticiones GET y POST
def user_api_view(request):
    if request.method == 'GET':

        # Consulta/queryset para obtener todos los usuarios del modelo usuario
        users = User.objects.all()
        users_serializers = UserSerializer(users, many=True)
       
        return Response(users_serializers.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            user_serializer.save() # Rgistrando usuario en la bdd
            
            return Response({'message':'Usuario creado correctamente'}, status=status.HTTP_201_CREATED)
        
        # Si el usuario no se crea, retorna un código bad request
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):

    # Consulta/queryset para obtener el usuario filtrado por id
    user = User.objects.filter(id=pk).first() 
    
    # Comprobando si el usuario existe if user es lo mismo que decir "si el usuario existe haz esto"
    if user:

        # Obteniendo los detalles de un usuario en especifico a través de un id de usuario
        if request.method == 'GET': 
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        
        # Modificando usuario especifico a través de su id
        elif request.method == 'PUT': 
            user_serializer = TestUserSerializer(user,data=request.data)

            if user_serializer.is_valid():
                user_serializer.save() # <== este save es del serializador, en este caso del serializador "TestUserSerializer"
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Eliminando usuario
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message':'Usuario eliminado correctamente'})
    
    # Si el usuario no existe, se retorna esta respuesta
    return Response({'message':'No se ha encontrado un usuario con los datos indicados'}, status=status.HTTP_400_BAD_REQUEST)