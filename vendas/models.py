from django.db import models
from clientes.models import Cliente
from colaboradores.models import Colaborador
from carros.models import Carro

class Venda(models.Model):
    situacao_choices = (
        ('P', 'processada'),
        ('C', 'cancelada'),
        ('F', 'finalizada'),
    )

    dataHora = models.DateTimeField()
    detalhes = models.CharField(max_length=50)
    valorVenda = models.DecimalField(max_digits=15, decimal_places=2)
    formaPagamento = models.CharField(max_length=20)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.SET_NULL, null=True)
    carro = models.ForeignKey(Carro, on_delete=models.SET_NULL, null=True)
    situacao = models.CharField(max_length=1, choices=situacao_choices, blank=False, null=False)

    def __str__(self) -> str:
        return self.detalhes