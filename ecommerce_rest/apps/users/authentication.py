from datetime import timedelta

from django.utils import timezone
from django.conf import settings

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class ExpiringTokenAuthentication(TokenAuthentication):
    expired = False

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
            # Refresacando el token automaticamente
            self.expired = True
            user = token.user
            token.delete()
            token = self.get_model().objects.create(user = token.user)
            
        return is_expire, token

    def authenticate_credentials(self, key):
        """
        Validando si el usuario está activo
        """

        message, token, user = None, None, None
        try:
            token = self.get_model().objects.select_related('user').get(key = key)
            user = token.user
        except self.get_model().DoesNotExist:
            message = "Token inválido"
            self.expired = True

        if token is not None:
            if not token.user.is_active:
                message = "Usuario no encontrado. Se ha elimiando o desactivado"
        
            is_expired, token = self.token_expire_handler(token)

            if is_expired:
                message = "Su token ha expirado"
        
        return (user, token, message, self.expired)
