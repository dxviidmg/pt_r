from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'passowrd': {'write_only': True}}

    def create(self, validated_data):

        print(validated_data)
        if validated_data['email'] == '':
            raise serializers.ValidationError("Email obligatorio")

        user =User(
            username = validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        
        return user