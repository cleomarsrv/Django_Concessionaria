from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Colaborador

def colaboradores(request):
    if request.method == "GET":
        colaboradores = Colaborador.objects.all()
        return render(request, 'colaboradores.html', {'colaboradores':colaboradores})
    if request.method == "POST":
        colaborador = Colaborador()

        colaborador.nomeCompleto = request.POST.get('nomeCompleto')
        colaborador.email = request.POST.get('email')
        colaborador.dataNascimento = request.POST.get('dataNascimento')
        colaborador.telefone = request.POST.get('telefone')
        colaborador.cpf = request.POST.get('cpf')
        colaborador.endereco = request.POST.get('endereco')
        colaborador.estadoCivil = request.POST.get('estadoCivil')
        colaborador.ctps = request.POST.get('ctps')
        colaborador.pis = request.POST.get('pis')
        colaborador.nomePai = request.POST.get('nomePai')
        colaborador.nomeMae = request.POST.get('nomeMae')
        colaborador.tipoVinculo = request.POST.get('tipoVinculo')
        colaborador.cargoAtual = request.POST.get('cargoAtual')
        colaborador.funcaoAtual = request.POST.get('funcaoAtual')
        colaborador.salarioAtual = request.POST.get('salarioAtual')
        colaborador.dataAdmissao = request.POST.get('dataAdmissao')
        colaborador.dataDesligamento = request.POST.get('dataDesligamento')
        colaborador.situacaoVinculo = request.POST.get('situacaoVinculo')

        try:
            colaborador.save()
            return redirect(reverse('colaboradores'))
        except:
            return HttpResponse('erro ao salvar')


def editar(request,id):
    colaborador = Colaborador.objects.get(id=id)
    return render(request, 'upd_colaborador.html', {'colaborador':colaborador})

def upd_colaborador(request, id):
    colaborador = Colaborador.objects.get(id=id)
    colaborador.nomeCompleto = request.POST.get('nomeCompleto')
    colaborador.email = request.POST.get('email')
    colaborador.dataNascimento = request.POST.get('dataNascimento')
    colaborador.telefone = request.POST.get('telefone')
    colaborador.cpf = request.POST.get('cpf')
    colaborador.endereco = request.POST.get('endereco')
    colaborador.estadoCivil = request.POST.get('estadoCivil')
    colaborador.ctps = request.POST.get('ctps')
    colaborador.pis = request.POST.get('pis')
    colaborador.nomePai = request.POST.get('nomePai')
    colaborador.nomeMae = request.POST.get('nomeMae')
    colaborador.tipoVinculo = request.POST.get('tipoVinculo')
    colaborador.cargoAtual = request.POST.get('cargoAtual')
    colaborador.funcaoAtual = request.POST.get('funcaoAtual')
    colaborador.salarioAtual = request.POST.get('salarioAtual')
    colaborador.dataAdmissao = request.POST.get('dataAdmissao')
    colaborador.dataDesligamento = request.POST.get('dataDesligamento')
    colaborador.situacaoVinculo = request.POST.get('situacaoVinculo')

    try:
        colaborador.save()
        return redirect(reverse('colaboradores'))
    except:
        return HttpResponse('erro ao salvar')
