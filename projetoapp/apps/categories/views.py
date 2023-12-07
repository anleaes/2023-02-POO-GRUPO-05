from django.shortcuts import render
from .models import Category
from .models import Cliente
from rest_framework import viewsets
from .serializer import CategorySerializer
from .serializer import ClienteSerializer

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer  

class ClienteListCreateView(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer