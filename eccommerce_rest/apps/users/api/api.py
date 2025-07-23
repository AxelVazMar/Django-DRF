from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer #,TestUserSerializer


    # def get(self, request): # Creando la petición HTTP 'GET'
        
    #     users = User.objects.all() # Haciendo consulta SQL 'FROM users SELECT *'
    #     users_serializers = UserSerializer(users, many=True) # Diciendole a DJANGO qué, debe listar. El 'many=True' es para decirle a DJANGO que debe listar todos los resultados de la consulta SQL
        
    #     return Response(users_serializers.data, status=status.HTTP_200_OK) # '.data' es para retornar la información serializada y convertida a JSON

@api_view(['GET', 'POST']) # Decorador @api_view para crear las peticiones GET y POST
def user_api_view(request):
    if request.method == 'GET':
        users = User.objects.all()
        users_serializers = UserSerializer(users, many=True)
        return Response(users_serializers.data)
    
    elif request.method == 'POST':
        print(request.data)