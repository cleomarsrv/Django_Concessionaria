from django.contrib import admin
from .models import Carro,Seguranca, Combustivel, Acessorio,Motor ,Direcao ,Versao

admin.site.register(Carro)
admin.site.register(Seguranca)
admin.site.register(Combustivel)
admin.site.register(Acessorio)
admin.site.register(Motor)
admin.site.register(Direcao)
admin.site.register(Versao)

