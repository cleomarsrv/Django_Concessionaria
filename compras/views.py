from django.shortcuts import render, redirect
from django.http import HttpResponse
from carros.models import Carro, Versao
from .models import Compra
from django.urls import reverse
from django.contrib import messages


def compras(request):
    if request.method == "GET":
        carros = Carro.objects.all()
        versoes = Versao.objects.all()
        compras = Compra.objects.all()
        context = {
            'carros':carros,
            'versoes':versoes,
            'compras':compras
        }
        return render(request, 'compras.html', context=context)
    elif request.method == "POST":
        versao_id = request.POST.get('versao')
        quantidade = request.POST.get('quantidade')

        compra = Compra()
        versao = Versao.objects.get(id=versao_id)
        compra.dataHora = request.POST.get('dataHora')
        compra.versao_id = versao_id
        compra.quantidade = quantidade
        compra.valorTotal = request.POST.get('valorTotal')
        
        versao.estoque += int(quantidade)

        try:
            compra.save()
            versao.save()
            messages.add_message(request, messages.constants.SUCCESS, 'compra efetuada com sucesso')
            return redirect(reverse('compras'))
        except:
            messages.add_message(request, messages.constants.ERROR, 'erro ao efetivar a compra, tente novamente.')
            return redirect(reverse('compras'))
    