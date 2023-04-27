from django.db import models

from cliente.models import Cliente
from prestador.models import Prestador


class Demanda(models.Model):
    cliente = models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL)
    prestador = models.ForeignKey(Prestador,  null=True, on_delete=models.SET_NULL)
    descricao = models.TextField(default='')
    quantidade_horas = models.IntegerField(default=0)
