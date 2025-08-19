from rest_framework.authtoken.views import ObtainAuthToken

class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class()