from .models import Carro, Versao, Seguranca, Direcao, Motor, Combustivel, Acessorio
from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from fornecedores.models import Fornecedor
from carros.forms import FormVersao

def carros(request, slugCarro=None):
    if request.method == "GET":
        carros = Carro.objects.all()
        try:
            carroSelecionado = Carro.objects.get(slugCarro=slugCarro)
            versoes = Versao.objects.filter(carro__id = carroSelecionado.id)
        except:
            carroSelecionado = None
            versoes = None
        
        if versoes:
            return redirect(reverse('versoes', kwargs={'slugVersao':None}))

        context = {
            'carros':carros,
            'versoes':versoes,
            'carroSelecionado':carroSelecionado,
        }
        return render(request, 'carros.html', context=context)
    elif request.method == "POST":
        nome = request.POST.get('nome')
        carro = Carro(
            nome = nome,
        )
        carro.save()
        messages.add_message(request, constants.SUCCESS, f'carro {nome} cadastrado com sucesso')
        messages.add_message(request, constants.INFO, 'cadastre agora uma versão:')
        slugCarro = carro.slugCarro
        return redirect(reverse('cadastrar_versao', kwargs={'slugCarro':slugCarro}))

def versoes(request, slugCarro):
    carroSelecionado = Carro.objects.get(slugCarro=slugCarro)
    versoes = Versao.objects.filter(carro__id=carroSelecionado.id)
    carros = Carro.objects.all()

    testeVersao =Versao.objects.get(id=1)

    context = {
        'versoes':versoes,
        'carroSelecionado':carroSelecionado,
        'carros':carros,
    }
    return render(request, 'carros_versoes.html', context=context)

def cadastrar_versao(request, slugCarro):
    carro = Carro.objects.get(slugCarro=slugCarro)
    if request.method == "GET":
        form = FormVersao()
        context = {
            'carro':carro,
            'form':form
        }
        return render(request, 'cadastrar_versao.html', context=context)
    elif request.method == "POST":
        form = FormVersao(request.POST)

    if form.is_valid():
        form.save()
        messages.add_message(request, constants.SUCCESS, 'versão cadastrada com sucesso.')
    else:
        context = {
            'carro':carro,
            'form':form
        }
        return render(request, 'cadastrar_versao.html', context=context)

    slugCarro = carro.slugCarro
    return redirect(reverse('versoes', kwargs={'slugCarro':slugCarro}))

def editar_carro(request,id):
    carro = Carro.objects.get(id=id)
    fornecedores = Fornecedor.objects.all()
    return render(request, 'upd_carro.html', {'carro':carro, 'fornecedores':fornecedores})

def upd_carro(request, id):
    carro = Carro.objects.get(id=id)
    placaCarro = request.POST.get('placaCarro')
    nomeCarro = request.POST.get('nomeCarro')
    combustivelCarro = request.POST.get('combustivelCarro')
    especificacaoCarro = request.POST.get('especificacaoCarro')
    fornecedor_id = request.POST.get('fornecedor')
    anoFabricacaoCarro = request.POST.get('anoFabricacaoCarro')
    anoModeloCarro = request.POST.get('anoModeloCarro')
    chassiCarro = request.POST.get('chassiCarro')
    
    carro.placaCarro = placaCarro
    carro.nomeCarro = nomeCarro
    carro.combustivelCarro = combustivelCarro
    carro.especificacaoCarro = especificacaoCarro
    carro.fornecedor_id = fornecedor_id
    carro.anoFabricacaoCarro = anoFabricacaoCarro
    carro.anoModeloCarro = anoModeloCarro
    carro.chassiCarro = chassiCarro
    carro.save()
    return redirect(reverse('carros'))