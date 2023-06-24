from django.db import models
from pessoas.models import Pessoa

class Colaborador(Pessoa):

    class Meta:
        verbose_name_plural = 'Colaboradores'
        permissions = (
            ('permissao_gerente', 'permissao gerente'),
            ('permissao_supervisor', 'permissao supervisor'),
            ('permissao_vendedor', 'permissao vendedor'),
            ('permissao_funcionario', 'permissao todos funcionarios'),
        )

    situacaoVinculoChoices = (
        ('A','Ativo'),
        ('I','Inativo'),
    )

    cargoAtualChoices = (
        ('V','vendedor'),
        ('S','supervisor'),
        ('G','gerente'),
    )

    funcaoAtualChoices = (
        ('N','Normal'),
        ('C','Comissionada'),
    )

    tipoVinculoChoices = (
        ('E','Experiencia'),
        ('C','Contratado'),
    )

    ctps = models.IntegerField()
    pis = models.IntegerField()
    nomePai = models.CharField(max_length=50, verbose_name='Pai')
    nomeMae = models.CharField(max_length=50, verbose_name='Mae')
    tipoVinculo = models.CharField(max_length=1, choices=tipoVinculoChoices, verbose_name='Tipo vinculo')
    cargoAtual = models.CharField(max_length=1, choices=cargoAtualChoices, verbose_name='Cargo atual')
    funcaoAtual = models.CharField(max_length=1, choices=funcaoAtualChoices, verbose_name='Funcao atual')
    salarioAtual = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Salario atual')
    dataAdmissao = models.DateField( verbose_name='Admissao')
    dataDesligamento = models.DateField(null=True, verbose_name='Desligamento')
    situacaoVinculo = models.CharField(max_length=1, choices=situacaoVinculoChoices, verbose_name='Situacao  vinculo')
