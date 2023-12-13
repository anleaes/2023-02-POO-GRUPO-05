from django.shortcuts import render
from .models import Loja
from rest_framework import viewsets
from .serializer import LojaSerializer

class LojaViewSet(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer