from django.db import models
from pessoas.models import Pessoa
from django.urls import reverse

class Cliente(Pessoa):
    renda = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='renda')
    profissao = models.CharField(max_length=20, verbose_name='profissao')

    class Meta:
        permissions = (('permissao_gerente', 'permissao gerente'),('permissao_vendedor', 'permissao vendendor'),)

    # def get_absolute_url(self):
    #     return reverse('clientes:clientes')
    