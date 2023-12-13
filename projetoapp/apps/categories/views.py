from django.shortcuts import render
from .models import Category, Cliente
from rest_framework import viewsets
from .serializer import CategorySerializer, ClienteSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ClienteListCreateView(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer