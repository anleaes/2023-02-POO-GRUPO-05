from django.db import models

class Carteira(models.Model):
    cnh = models.CharField(max_length=255)

    def __str__(self):
        return self.cnh