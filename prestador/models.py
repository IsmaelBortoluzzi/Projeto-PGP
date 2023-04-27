from django.db import models
from django.contrib.auth.models import User


class Prestador(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valor = models.DecimalField(default=0.0, blank=True, decimal_places=2, max_digits=12)
    documento = models.CharField(max_length=14, unique=True)
    chave_pix = models.CharField(max_length=255, blank=True, null=True, default='')
    comissao = models.DecimalField(default=0.0, blank=True, decimal_places=2, max_digits=12)  # 12.7 = 12.7%, ou seja, divida por 100 ao usar
