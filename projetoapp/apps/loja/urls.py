from django.urls import path, include
from rest_framework import routers
from .views import LojaViewSet

app_name = 'loja'

router = routers.DefaultRouter()
router.register('', LojaViewSet, basename='loja')

urlpatterns = [
    path('', include(router.urls)),
]