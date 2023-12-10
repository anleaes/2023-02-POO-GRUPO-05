from django.db import models

from django.db import models

class Locacao(models.Model):
    data_retirada = models.DateField('Data de Retirada')
    hora_retirada = models.TimeField('Hora de Retirada')
    data_devolucao = models.DateField('Data de Devolução')
    hora_devolucao = models.TimeField('Hora de Devolução')
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Locação'
        verbose_name_plural = 'Locações'
        ordering = ['id']

    def __str__(self):
        return f'Locacao {self.id}'