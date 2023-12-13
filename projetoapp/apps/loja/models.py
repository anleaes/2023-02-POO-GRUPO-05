from django.db import models
from veiculos.models import Veiculo 

class Loja(models.Model):
    endereco = models.CharField('Endereço', max_length=100)
    gerente = models.CharField('Gerente', max_length=50)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Loja'
        verbose_name_plural = 'Lojas'
        ordering = ['id']

    def __str__(self):
        return f'Loja {self.id}'