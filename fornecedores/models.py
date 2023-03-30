from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=30)
    cnpj = models.CharField(max_length=14)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    enderecoCompleto = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nome
