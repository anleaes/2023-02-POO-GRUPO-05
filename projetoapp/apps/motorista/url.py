from django.urls import path, include
from rest_framework import routers
from .views import MotoristaViewSet

app_name = 'motorista'

router = routers.DefaultRouter()
router.register('', MotoristaViewSet, basename='motorista')

urlpatterns = [
    path('', include(router.urls)),
]