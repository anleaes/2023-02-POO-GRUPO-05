"""projetoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('carteira/', include('carteira.url', namespace='carteira')),
    path('clients/', include(('clients.urls', 'clientes'), namespace='clientes')),
    path('formapagamento/', include('formapagamento.urls', namespace='formapagamento')),
    path('funcionarios/', include(('funcionarios.url', 'funcionarios'), namespace='funcionarios')),
    path('locacao/', include('locacao.urls', namespace='locacao')),
    path('loja/', include('loja.urls', namespace='loja')),
    path('motorista/', include('motorista.url', namespace='motorista')),
    path('veiculos/', include(('veiculos.url', 'veiculos'), namespace='veiculos')),

]
