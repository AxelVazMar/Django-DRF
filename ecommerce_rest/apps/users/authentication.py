from datetime import timedelta

from django.utils import timezone
from django.conf import settings

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class ExpiringTokenAuthentication(TokenAuthentication):

    def expires_in(self, token):
        """
        Calcula el tiempo de expiración del token
        """
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds = settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time

    def is_token_expired(self, token):
        """
        Ssber si el token ha expirado
        """
        return self.expires_in(token) < timedelta(seconds = 0)

    def token_expire_handler(self, token):
        """
        Inicia la ejecución en cadema de is_token_expired()
        """
        is_expire = self.is_token_expired(token)
        if is_expire:
            print("Token expirado")
            
        return is_expire

    def authenticate_credentials(self, key):
        """
        Validando si el usuario está activo
        """
        try:
            token = self.get_model().objects.select_related('user').get(key = key)
        except self.get_model().DoesNotExist:
            raise AuthenticationFailed('Token inválido')
        
        if not token.user.is_active:
            raise AuthenticationFailed('Usuario no válido. Se eliminó o no está activo')
        
        is_expired = self.token_expire_handler(token)

        if is_expired:
            raise AuthenticationFailed('Su token ha expirado')
        
        return (token.user, token)
