from django.db import models
from carros.models import Versao

class Compra(models.Model):

    class Meta:
        permissions = (
            ('permissao_gerente', 'permissao gerente'),
            ('permissao_supervisor', 'permissao supervisor'),
            ('permissao_vendedor', 'permissao vendedor'),
            ('permissao_funcionario', 'permissao todos funcionarios'),
        )
    dataHora = models.DateTimeField()
    versao = models.ForeignKey(Versao, on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField()
    valorTotal = models.FloatField()

    def __str__(self):
        return (f'{self.versao} - {self.dataHora}')