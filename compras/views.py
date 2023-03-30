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
        return render(request, 'compras.html', {'fornecedores':fornecedores, 'carros':carros})
    elif request.method == "POST":
        compra = Compra()
        compra.dataHora = request.POST.get('dataHora')
        compra.carro_id = request.POST.get('carro')
        compra.fornecedor_id = request.POST.get('fornecedor')
        compra.quantidade = request.POST.get('quantidade')
        compra.valorTotal = request.POST.get('valorTotal')
        try:
            compra.save()
            return redirect(reverse('compras'))
        except:
            return HttpResponse('erro ao efetivar a compra')