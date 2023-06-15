from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Venda
from carros.models import Carro
from clientes.models import Cliente
from colaboradores.models import Colaborador
from django.contrib import messages

def vendas(request):
    if request.method == "GET":
        vendas =  Venda.objects.all()
        clientes = Cliente.objects.all()
        carros = Carro.objects.all()
        colaboradores = Colaborador.objects.all()
        return render(request, 'vendas.html', {'vendas':vendas,'clientes':clientes,'carros':carros, 'colaboradores':colaboradores})
    elif request.method == "POST":
        carro_id = request.POST.get('carro_id')
        carro = Carro.objects.get(id=carro_id)
        if carro.estoque > 0:
            venda = Venda()
            venda.dataHora = request.POST.get('dataHora')
            venda.detalhes = request.POST.get('detalhes')
            venda.cliente_id = request.POST.get('cliente')
            venda.carro_id = carro_id
            venda.colaborador_id = request.POST.get('colaborador')
            venda.valorVenda = request.POST.get('valorVenda')
            venda.formaPagamento = request.POST.get('formaPagamento')
            venda.situacao = 'P'
            carro.estoque -= 1
            try:
                venda.save()
                carro.save()
                messages.add_message(request, messages.SUCCESS, 'venda efetuada com sucesso!')
                return redirect(reverse('vendas'))
            except:
                messages.add_message(request, messages.ERROR, 'erro ao efetivar a venda' )
                return redirect(reverse('vendas'))
            
        else:
            messages.add_message(request, messages.ERROR, f' Nao há estoque do carro {carro.nomeCarro}')
            return redirect(reverse('vendas'))

def editar(request, id):
    return HttpResponse('editando venda')
