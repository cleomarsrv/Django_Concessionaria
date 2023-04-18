from .models import Carro, Versao, Seguranca, Direcao, Motor, Combustivel, Acessorio
from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from fornecedores.models import Fornecedor

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
            return redirect(reverse('versoes'))

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
        messages.add_message(request, constants.SUCCESS, 'carro cadastrado com sucesso')
        return redirect(reverse('carros'))

def versoes(request,slugVersao=None):
    if request.method == "GET":
        idTeste = 1
        carroSelecionado = Carro.objects.get(id=idTeste)
        versoes = Versao.objects.filter(carro__id=idTeste)
        carros = Carro.objects.all()
    
        context = {
            'versoes':versoes,
            # 'carroSelecionado':carroSelecionado,
            'carros':carros,
        }
        return HttpResponse(f'mostrando slugVersao = {slugVersao}')
        #return render(request, 'carros.html', context=context)
    elif request.method == "POST":
        return HttpResponse('estou em versoes via metodo POST')

def cadastrar_versao(request, id):
    if request.method == "GET":
        carro = Carro.objects.get(id=id)

        segurancas = Seguranca.objects.all()
        direcoes = Direcao.objects.all()
        motores = Motor.objects.all()
        combustiveis = Combustivel.objects.all()
        acessorios = Acessorio.objects.all()
        
        context = {
            'carro':carro,
            'segurancas':segurancas,
            'direcoes':direcoes,
            'motores':motores,
            'combustiveis':combustiveis,
            'acessorios':acessorios,
        }
        return render(request, 'cadastrar_versao.html', context=context)
    elif request.method == "POST":
        nome = request.POST.get('nome')
        imagem = request.FILES.get('imagem')
        
        segurancas = request.POST.getlist('seguranca')
        
        direcao = request.POST.get('direcao')
        carro = id
        motor = request.POST.get('motor')
        combustivel = request.POST.get('combustivel')
        acessorios = request.POST.getlist('acessorio')

        versao = Versao(
            nome = nome,
            imagem = imagem,
            #seguranca = seguranca,
            direcao_id = direcao,
            carro_id = carro,
            motor_id = motor,
            combustivel_id = combustivel,
            #acessorio = acessorio,
        )

        versao.save()

        return redirect(reverse('carros'))


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