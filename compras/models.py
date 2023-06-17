from django.db import models
from carros.models import Versao
from fornecedores.models import Fornecedor

class Compra(models.Model):
    dataHora = models.DateTimeField()
    versao = models.ForeignKey(Versao, on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField()
    valorTotal = models.FloatField()

    def __str__(self):
        return (f'{self.versao} - {self.dataHora}')