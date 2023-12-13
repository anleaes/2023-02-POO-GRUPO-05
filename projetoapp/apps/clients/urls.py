from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'clients'

router = routers.DefaultRouter()
router.register('', views.ClientViewSet, basename='clientes')
router.register('socialnetworks', views.ClientSocialnetworkViewSet, basename='client-socialnetworks')  # Ajuste aqui

urlpatterns = [
    path('', include(router.urls)),
]