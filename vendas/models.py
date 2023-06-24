from django.db import models
from clientes.models import Cliente
from colaboradores.models import Colaborador
from carros.models import Versao

class Venda(models.Model):

    class Meta:
        permissions = (
            ('permissao_gerente', 'permissao gerente'),
            ('permissao_supervisor', 'permissao supervisor'),
            ('permissao_vendedor', 'permissao vendedor'),
            ('permissao_funcionario', 'permissao todos funcionarios'),
        )
    situacaoChoices = (
        ('P', 'processada'),
        ('C', 'cancelada'),
        ('F', 'finalizada'),
    )

    formaPagamentoChoices = (
        ('e','especie'),
        ('t','transferencia bancaria'),
        ('c','consorcio'),
    )

    dataHora = models.DateTimeField()
    detalhes = models.CharField(max_length=50)
    valorVenda = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Valor')
    formaPagamento = models.CharField(max_length=1, choices=formaPagamentoChoices, verbose_name='Pagamento')
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.DO_NOTHING)
    versao = models.ForeignKey(Versao, on_delete=models.DO_NOTHING)
    situacao = models.CharField(max_length=1, choices=situacaoChoices)    

    def __str__(self) -> str:
        return self.detalhes