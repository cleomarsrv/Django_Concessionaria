from django.shortcuts import render, redirect
from django.http import HttpResponse
from fornecedores.models import Fornecedor
from carros.models import Carro
from .models import Compra
from django.urls import reverse

def compras(request):
    if request.method == "GET":
        fornecedores = Fornecedor.objects.all()
        carros = Carro.objects.all()
        compras = Compra.objects.all()
        context = {
            'fornecedores':fornecedores,
            'carros':carros,
            'compras':compras
        }
        return render(request, 'compras.html', context=context)
    elif request.method == "POST":
        carro_id = request.POST.get('carro')
        quantidade = request.POST.get('quantidade')

        compra = Compra()
        carro = Carro.objects.get(id=carro_id)
        compra.dataHora = request.POST.get('dataHora')
        compra.carro_id = carro_id
        compra.fornecedor_id = request.POST.get('fornecedor')
        compra.quantidade = quantidade
        compra.valorTotal = request.POST.get('valorTotal')
        
        carro.estoque += int(quantidade)

        try:
            compra.save()
            carro.save()
            return redirect(reverse('compras'))
        except:
            return HttpResponse('erro ao efetivar a compra')
        
    