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

    def create(self, validated_data):

        # encriptando contraseña a través de un serializer
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save() # <== método save del modelo "User"
        return user
    
    def update(self, instance, validated_data):

        # actualizando la contraseña de un usuario que ya estaba registrado para encriptarla
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user

class UserListSerializer(serializers.ModelSerializer):
    """
    Este serializador lista los Usuarios y les "da" una forma personalizada para mostrarlos
    """

    class Meta:
        model = User

    def to_representation(self, instance):
        return {
            "id":instance['id'],
            "username":instance['username'],
            "email":instance['email'],
            "password":instance['password']
        }

class UserTokenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name')