from django.urls import path, include
from rest_framework import routers
from .views import CarteiraViewSet

app_name = 'carteira'

router = routers.DefaultRouter()
router.register('', CarteiraViewSet, basename='carteira')

urlpatterns = [
    path('', include(router.urls)),
]