from django.db import models
from pessoas.models import Pessoa

class Colaborador(Pessoa):

    class Meta:
        verbose_name_plural = 'Colaboradores'

    ctps = models.IntegerField()
    pis = models.IntegerField()
    nomePai = models.CharField(max_length=50)
    nomeMae = models.CharField(max_length=50)
    tipoVinculo = models.CharField(max_length=20)
    cargoAtual = models.CharField(max_length=20)
    funcaoAtual = models.CharField(max_length=20)
    salarioAtual = models.DecimalField(max_digits=15, decimal_places=2)
    dataAdmissao = models.DateField()
    dataDesligamento = models.DateField(null=True)
    situacaoVinculo = models.CharField(max_length=20)
