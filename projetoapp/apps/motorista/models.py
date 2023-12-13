from django.db import models

from django.db import models
from carteira.models import Carteira 

class Motorista(models.Model):
    nome = models.CharField('Nome', max_length=50)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    carteira = models.OneToOneField(Carteira, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Motorista'
        verbose_name_plural = 'Motoristas'
        ordering = ['id']

    def __str__(self):
        return self.nome