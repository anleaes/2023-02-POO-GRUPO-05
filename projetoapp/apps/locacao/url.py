from django.urls import path, include
from rest_framework import routers
from .views import LocacaoListCreateView

app_name = 'locacoes'

router = routers.DefaultRouter()
router.register('', LocacaoListCreateView, basename='locacoes')

urlpatterns = [
    path('', include(router.urls)),
]