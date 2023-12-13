from rest_framework import serializers
from .models import Locacao

class LocacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locacao
        fields = '__all__'
