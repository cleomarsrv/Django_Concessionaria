from django.db import models

class Marca(models.Model):
    nomeMarca = models.CharField(max_length=30)
    cnpjMarca = models.CharField(max_length=14)

    def __str__(self) -> str:
        return self.nomeMarca

class Fornecedor(models.Model):
    nomeFornecedor = models.CharField(max_length=30)
    cnpjFornecedor = models.CharField(max_length=14)
    marcaFornecida = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True)
    emailFornecedor = models.EmailField()
    enderecoFornecedor = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nomeFornecedor
