from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Venda
from carros.models import Carro
from clientes.models import Cliente
from colaboradores.models import Colaborador

def vendas(request):
    if request.method == "GET":
        vendas =  Venda.objects.all()
        clientes = Cliente.objects.all()
        carros = Carro.objects.all()
        colaboradores = Colaborador.objects.all()
        return render(request, 'vendas.html', {'vendas':vendas,'clientes':clientes,'carros':carros, 'colaboradores':colaboradores})
    elif request.method == "POST":
        venda = Venda()

        venda.dataHora = request.POST.get('dataHora')
        venda.detalhes = request.POST.get('detalhes')
        venda.cliente_id = request.POST.get('cliente')
        venda.carro_id = request.POST.get('carro')
        venda.colaborador_id = request.POST.get('colaborador')
        venda.valorVenda = request.POST.get('valorVenda')
        venda.formaPagamento = request.POST.get('formaPagamento')

        try:
            venda.save()
            return redirect(reverse('vendas'))
        except:
            return HttpResponse('erro ao efetivar a venda')


def editar_venda(request, id):
    return HttpResponse('editando venda')
