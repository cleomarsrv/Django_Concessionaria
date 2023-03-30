from django.db import models
from carros.models import Carro
from fornecedores.models import Fornecedor

class Compra(models.Model):
    dataHora = models.DateTimeField()
    carro = models.ForeignKey(Carro, on_delete=models.SET_NULL, null=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True)
    quantidade = models.IntegerField()
    valorTotal = models.FloatField()

    def __str__(self):
        return (f'{self.carro} - {self.dataHora}')
