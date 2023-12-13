from django.shortcuts import render
from .models import Motorista
from rest_framework import viewsets
from .serializer import MotoristaSerializer

class MotoristaViewSet(viewsets.ModelViewSet):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer