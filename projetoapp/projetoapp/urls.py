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
    path('formapagamento/', include('formapagamento.urls', namespace='formapagamento')),
    path('products/', include('products.urls', namespace='produtos')),
    path('categories/', include('categories.urls', namespace='categorias')),
    path('clients/', include('clients.urls', namespace='clientes')),
    path('socialnetworks/', include('socialnetworks.urls', namespace='midias')),
    # path('locacao/', include('locacao.urls')),
    # path('loja/', include('loja.urls')),
    # path('motorista/', include('motorista.urls')),
    # path('orders/', include('orders.urls')),
    # path('locacao/', include('locacao.urls', namespace='locacao')),

]
