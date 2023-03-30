from django.db import models
from fornecedores.models import Fornecedor

class Carro(models.Model):
    placaCarro = models.CharField(max_length=7)
    nomeCarro = models.CharField(max_length=30)
    combustivelCarro = models.CharField(max_length=20)
    especificacaoCarro = models.CharField(max_length=100)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True)
    anoFabricacaoCarro = models.IntegerField()
    anoModeloCarro = models.IntegerField()
    chassiCarro = models.CharField(max_length=17)
    estoque = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.nomeCarro