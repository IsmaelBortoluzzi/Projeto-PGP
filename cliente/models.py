from django.db import models


class Cliente(models.Model):
    documento = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=16, null=True, blank=True, default='')
    email = models.EmailField(max_length=255, default='')
