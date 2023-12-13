from django.shortcuts import render
from rest_framework import viewsets
from .models import Locacao
from .serializer import LocacaoSerializer

class LocacaoViewSet(viewsets.ModelViewSet):
    queryset = Locacao.objects.all()
    serializer_class = LocacaoSerializer