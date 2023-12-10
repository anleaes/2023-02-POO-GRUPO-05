from django.shortcuts import render
from .models import FormaPagamento
from rest_framework import viewsets
from .serializer import FormaPagamentoSerializer

# Create your views here.
class FormaPagamentoListCreateView(viewsets.ListCreateAPIView):
    queryset = FormaPagamento.objects.all()
    serializer_class = FormaPagamentoSerializer