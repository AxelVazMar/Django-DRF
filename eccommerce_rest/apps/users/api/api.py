from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.models import User
from apps.users.api.serializers import UserSerializer, TestUserSerializer

class UserAPIView(APIView):

    def get(self, request): # Creando la petición HTTP 'GET'
        
        users = User.objects.all() # Haciendo consulta SQL 'FROM users SELECT *'
        users_serializers = UserSerializer(users, many=True) # Diciendole a DJANGO qué, debe listar. El 'many=True' es para decirle a DJANGO que debe listar todos los resultados de la consulta SQL

        test_data = {
            'name':'axel',
            'email':'axelvazmar@gmail.com'
        }
        
        test_user = TestUserSerializer(data = test_data,context = test_data)

        if test_user.is_valid():
            print("Pasó validaciones")
        else:
            print(test_user.errors) # ".errors" mete los errores en las validaciones en un diccionario
        
        return Response(users_serializers.data, status=status.HTTP_200_OK) # '.data' es para retornar la información serializada y convertida a JSON