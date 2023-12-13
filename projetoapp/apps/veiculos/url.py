from django.urls import path, include
from rest_framework import routers
from .views import VeiculoViewSet

router = routers.DefaultRouter()
router.register('', VeiculoViewSet, basename='veiculos')

urlpatterns = [
    path('', include(router.urls)),
]