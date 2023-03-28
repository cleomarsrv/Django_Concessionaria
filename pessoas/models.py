from django.db import models

class Pessoa(models.Model):
    class Meta:
        abstract = True
    nomeCompleto = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    dataNascimento = models.DateField()
    telefone = models.CharField(max_length=12)
    cpf = models.CharField(max_length=11, unique=True)
    endereco = models.CharField(max_length=100)
    estadoCivil = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nomeCompleto
    
'''
nomeCompleto
email
dataNascimento
telefone
cpf
endereco
estadoCivil
'''