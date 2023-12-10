from django.db import models

# Create your models here.
from django.db import models

class Carteira(models.Model):
    cnh = models.CharField('CNH', max_length=9)

    class Meta:
        verbose_name = 'Carteira'
        verbose_name_plural = 'Carteiras'
        ordering = ['id']

    def __str__(self):
        return f'Carteira {self.id}'