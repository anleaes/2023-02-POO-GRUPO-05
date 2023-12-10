from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'carteira'

router = routers.DefaultRouter()
router.register('', views.ProductViewSet, basename='carteira')

urlpatterns = [
    path('', include(router.urls) )
]