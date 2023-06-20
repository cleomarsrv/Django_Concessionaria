from django.db import models
from fornecedores.models import Fornecedor
from django.template.defaultfilters import slugify

class Seguranca(models.Model):
    item = models.CharField(max_length=50)

    def __str__(self):
        return self.item
    
class Combustivel(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo
    
    class Meta:
        verbose_name_plural = 'Combustiveis'
    
class Acessorio(models.Model):
    item = models.CharField(max_length=50)

    def __str__(self):
        return self.item
    
class Motor(models.Model):
    nome = models.CharField(max_length=50)
    cv = models.IntegerField()
    torque = models.FloatField()
    rpm = models.IntegerField()
    valvulas = models.IntegerField()
    cilindros = models.IntegerField(default=3)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'Motores'

class Direcao(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo
    
    class Meta:
        verbose_name_plural = 'Direcoes'

class Carro(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    slugCarro = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slugCarro:
            self.slugCarro = slugify(self.nome)
        return super().save(*args, **kwargs)
    
    class Meta:
        permissions = (
            ('permissao_gerente', 'permissao gerente'),
            ('permissao_supervisor', 'permissao supervisor'),
            ('permissao_vendedor', 'permissao vendendor'),
            ('permissao_funcionario', 'permissao todos funcionarios'),
        )
    
class Versao(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=50, unique=True)
    motor = models.ForeignKey(Motor, on_delete=models.DO_NOTHING)
    combustivel = models.ForeignKey(Combustivel, on_delete=models.DO_NOTHING)
    direcao = models.ForeignKey(Direcao, on_delete=models.DO_NOTHING)
    seguranca = models.ManyToManyField(Seguranca, related_name="versao_seguranca", blank=True)
    acessorio = models.ManyToManyField(Acessorio, related_name="versao_acessorio", blank=True)
    imagem = models.ImageField(upload_to='carros', blank=True, null=True)
    ano = models.IntegerField(default='2023')
    modelo = models.IntegerField(default='2023')
    estoque = models.IntegerField(default=0) 
    slugVersao = models.SlugField(unique=True, null=True, blank=True)

    class Meta:
        permissions = (
            ('permissao_gerente', 'permissao gerente'),
            ('permissao_vendedor', 'permissao vendendor'),
            ('permissao_funcionario', 'permissao todos funcionarios'),
        )

    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        if not self.slugVersao:
            self.slugVersao = slugify(self.nome)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Versoes'
    
    