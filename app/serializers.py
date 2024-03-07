from rest_framework import serializers
from .models import *

from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class ReceptListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipes
        fields = ('id','title','description','created_date')

class ReceptDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipes
        fields = "__all__"

class ReceptUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipes
        fields = '__all__'

class ReceptDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipes
        fields = '__all__'

class ReceptCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    class Meta:
        model = Receipes
        fields = ('__all__')




class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')




class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            if field == 'password':
                instance.set_password(value)
            else:
                setattr(instance, field, value)

        instance.save()
        return instance
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(
                request=self.context.get('request'),
                username=username,
                password=password
            )
            if not user:
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user  
        return attrs
