from django.shortcuts import render
from .models import Carteira
from rest_framework import viewsets
from .serializer import CarteiraSerializer

class CarteiraViewSet(viewsets.ModelViewSet):
    queryset = Carteira.objects.all()
    serializer_class = CarteiraSerializer