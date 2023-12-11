from django.urls import path, include
from rest_framework import routers
from .views import LocacaoListCreateView

app_name = 'locacao'

router = routers.DefaultRouter()
router.register('', LocacaoListCreateView, basename='locacao')

urlpatterns = [
    path('', include(router.urls)),
]