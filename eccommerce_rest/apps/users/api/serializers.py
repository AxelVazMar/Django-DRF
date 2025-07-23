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
            raise serializers.ValidationError('The user needs an email')
        
        # if self.context['name'] in value:
        #     raise serializers.ValidationError('El email no puede contener el nombre')

        return value
    
    def validate(self, data):
        """
        Method to validate the data of a user
        """
    
        return data
    
    def create(self, validated_data):
        """
        Method to create a user when the data is valid
        """
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.email = validated_data.get('email',instance.email)
        instance.save()
        return instance