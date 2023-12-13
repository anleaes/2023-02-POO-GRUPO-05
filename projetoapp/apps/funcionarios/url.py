from django.urls import path, include
from rest_framework import routers
from .views import FuncionarioViewSet

router = routers.DefaultRouter()
router.register('', FuncionarioViewSet, basename='funcionarios')

urlpatterns = [
    path('', include(router.urls)),
]