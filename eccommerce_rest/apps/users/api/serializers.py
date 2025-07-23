from rest_framework import serializers
from apps.users.models import User

# Se se le pasa el ModelSerializer ya que va a ser un serializer basado en un modelo usuario
class UserSerializer(serializers.ModelSerializer):
    """
    Este serializador convierte cualquier estructura del modelo 'User' a JSON
    """
    class Meta:
        model = User
        fields = '__all__'

class TestUserSerializer(serializers.Serializer):
    """
    This serializer is for making customs validations
    """

    name = serializers.CharField(max_length = 200)
    email = serializers.EmailField()

    def validate_name(self, value):

        # creating custom validation for name field
        if 'dev' in value:
            raise serializers.ValidationError("Error, a user with that name can't exists")
        return value
    
    def validate_email(self, value):

        # creting a custom validation for email field
        if value == '':
            raise serializers.ValidationError('The user need a email')
        
        if self.context['name'] in value:
            raise serializers.ValidationError('El email no puede contener el nombre')

        return value
    
    def validate(self, data):
    
        return data