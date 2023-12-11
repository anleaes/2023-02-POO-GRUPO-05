from django.db import models

# Create your models here.

class Loja(models.Model):
    endereco = models.TextField()
    gerente = models.CharField(max_length=100)
    veiculo = models.OneToOneField(Veiculo, on_delete=models.SET_NULL, null=True, blank=True)
    motoristas = models.ManyToManyField(Motorista)

    class Meta:
        verbose_name = 'Loja'
        verbose_name_plural = 'Lojas'
        ordering = ['id']

    def __str__(self):
        return f'Loja em {self.endereco} gerenciada por {self.gerente}'