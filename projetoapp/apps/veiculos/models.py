from django.db import models
from formapagamento.models import FormaPagamento

class Veiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)
    km = models.FloatField()
    categoria = models.CharField(max_length=50)
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.marca} {self.modelo}"