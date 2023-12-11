from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Locacao
from .serializers import LocacaoSerializer

class LocacaoListCreateView(generics.ListCreateAPIView):
    queryset = Locacao.objects.all()
    serializer_class = LocacaoSerializer