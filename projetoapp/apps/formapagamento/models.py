from django.db import models

class FormaPagamento(models.Model):
    credito_vista = models.BooleanField('Crédito à vista')
    credito_parcelado = models.BooleanField('Crédito parcelado')
    debito = models.BooleanField('Débito')
    pix = models.BooleanField('PIX')
    cheque = models.BooleanField('Cheque')

    class Meta:
        verbose_name = 'Forma de Pagamento'
        verbose_name_plural = 'Formas de Pagamento'
        ordering = ['id']

    def __str__(self):
        return f'FormaPagamento {self.id}'