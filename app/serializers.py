from rest_framework import serializers
from .models import *

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