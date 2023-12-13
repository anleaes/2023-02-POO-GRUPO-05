from django.db import models
from clients.models import Cliente
from funcionarios.models import Funcionario
from loja.models import Loja
from formapagamento.models import FormaPagamento
from veiculos.models import Veiculo
from carteira.models import Carteira
from motorista.models import Motorista

class Locacao(models.Model):
    data_retirada = models.DateField()
    hora_retirada = models.TimeField()
    data_devolucao = models.DateField()
    hora_devolucao = models.TimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    carteira = models.ForeignKey(Carteira, on_delete=models.CASCADE)

    def __str__(self):
        return f"Locacao {self.id}"