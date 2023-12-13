from django.shortcuts import render
from .models import FormaPagamento
from rest_framework import viewsets
from .serializer import FormaPagamentoSerializer

class FormaPagamentoViewSet(viewsets.ModelViewSet):
    queryset = FormaPagamento.objects.all()
    serializer_class = FormaPagamentoSerializer