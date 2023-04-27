from django.db import models

from demanda.models import Demanda


class OrdemServico(models.Model):
    demanda = models.ForeignKey(Demanda, null=True, on_delete=models.SET_NULL)
    processo = models.CharField(max_length=16, default='')
    status = models.CharField(max_length=16, default='')
