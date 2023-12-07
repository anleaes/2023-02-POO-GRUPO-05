from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering =['id']

    def __str__(self):
        return self.name
    
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=50)
    endereco = models.TextField('Endereco', max_length=100)
    genero = models.CharField('Genero H ou M', max_length=1)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

    def __str__(self):
        return self.nome