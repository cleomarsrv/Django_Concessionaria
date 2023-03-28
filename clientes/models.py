from django.db import models
from pessoas.models import Pessoa

class Cliente(Pessoa):
    renda = models.DecimalField(max_digits=15, decimal_places=2)
    profissao = models.CharField(max_length=20)
