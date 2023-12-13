from rest_framework import serializers
from .models import FormaPagamento

class FormaPagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPagamento
        fields = ['id', 'credito_vista', 'credito_parcelado', 'debito', 'pix', 'cheque']
