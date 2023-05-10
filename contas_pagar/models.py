from django.db import models

from demanda.models import Demanda

class ContasPagar(models.Model):
    demanda = models.ForeignKey(Demanda, null=True, on_delete=models.SET_NULL)
    valor = models.DecimalField(default=0.0, decimal_places=2, max_digits=12)
    data_criacao = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=16)