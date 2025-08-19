from datetime import datetime
from django.contrib.sessions.models import Session

from rest_framework import status
from rest_framework.response import Response 
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from apps.users.api.serializers import UserTokenSerializer

class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request':request})
        if login_serializer.is_valid(): # <== validando que exista un usuario y contraseña en la bdd
            user = login_serializer.validated_data['user']

            if user.is_active:
                token,created = Token.objects.get_or_create(user = user) # Diciendole que si el usuario está activo entonces asignale o creale un token. 'created' es un bool, si se creó un nuevo token es True sino es False
                user_serializer = UserTokenSerializer(user)
                if created: # si created es True
                    return Response({
                        'token':token.key,
                        'user':user_serializer.data,
                        'message':'Inicio de sesión exitoso'
                    }, status=status.HTTP_201_CREATED)
                else:
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now()) # Estamos diciendo que obtenga todas las sesiones que están por expirar gte es "grather than or equal" ósea mayor o igual que
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                                # Si un usuario ya tiene una sesión activa y vuelve a iniciar sesión en otro lugar, se le borrará la sesión
                    token.delete()
                    token = Token.objects.create(user = user) 
                    return Response({
                        'token':token.key,
                        'user':user_serializer.data,
                        'message':'Inicio de sesión exitoso'
                    }, status=status.HTTP_201_CREATED)
            else:
                return Response({'error':'Este usuario no puede loggearse'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error':'nombre de usuario o contraseña incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'message':'Hola desde response'}, status=status.HTTP_200_OK)