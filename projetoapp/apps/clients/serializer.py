from rest_framework import serializers
from .models import Client, ClientSocialnetwork

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ClientSocialnetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientSocialnetwork
        fields = '__all__'