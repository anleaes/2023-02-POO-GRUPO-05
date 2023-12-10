from .models import Carteira
from rest_framework import serializers

class CarteiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carteira
        fields = '__all__'