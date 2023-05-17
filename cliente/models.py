from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=16, unique=False)
    documento = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=16, null=True, blank=True, default='')
    email = models.EmailField(max_length=255, default='')

    def __str__(self) -> str:
        return self.nome
