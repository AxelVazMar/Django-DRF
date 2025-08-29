from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import get_authorization_header

from apps.users.authentication import ExpiringTokenAuthentication

class Authentication(object):
    user = None
    user_token_expired = False

    def get_user(self, request):
        """
        Validando si nos envían un token inválido
        """
        token = get_authorization_header(request).split()
        
        if token:
            try:
                token = token[1].decode()
            except: 
                return None
        
            token_expire = ExpiringTokenAuthentication() 
            user, token, message, expired = token_expire.authenticate_credentials(token)
            self.user_token_expired = expired
            
            if user != None and token != None:
                self.user = user
                return user
            return message
        return None

    def dispatch(self, request, *args, **kwargs):
        user = self.get_user(request)
        # token encontrado en el request
        if user is not None:
            if type(user) == str:
                response = Response({'error':user, 
                                     'expired':self.user_token_expired}, status=status.HTTP_400_BAD_REQUEST)
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = 'application/json'
                response.renderer_context = {}
                return response

            return super().dispatch(request, *args, **kwargs)
        
        response = Response({'error': 'No se han enviado las credenciales',
                             'expired':self.user_token_expired}, status=status.HTTP_400_BAD_REQUEST) 
        # No se puede retornar directamente el response, debe ser con una variable
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'application/json'
        response.renderer_context = {}
        return response