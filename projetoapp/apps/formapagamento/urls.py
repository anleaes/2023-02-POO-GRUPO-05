from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'formapagamento'

router = routers.DefaultRouter()
router.register('', views.ProductViewSet, basename='pagamento')

urlpatterns = [
    path('', include(router.urls) )
]