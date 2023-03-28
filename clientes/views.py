from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Cliente

def clientes(request):
    if request.method == "GET":
        clientes = Cliente.objects.all()
        return render(request, 'clientes.html', {'clientes':clientes})
    elif request.method == "POST":
        
        '''cliente  = Cliente()
        cliente.nomeCompleto = request.POST.get('nomeCompleto')
        cliente.email = request.POST.get('email')
        cliente.dataNascimento = request.POST.get('dataNascimento')
        cliente.telefone = request.POST.get('telefone')
        cliente.cpf = request.POST.get('cpf')
        cliente.endereco = request.POST.get('endereco')
        cliente.estadoCivil = request.POST.get('estadoCivil')
        cliente.renda = request.POST.get('renda')
        cliente.profissao = request.POST.get('profissao')'''

        nomeCompleto = request.POST.get('nomeCompleto')
        email = request.POST.get('email')
        dataNascimento = request.POST.get('dataNascimento')
        telefone = request.POST.get('telefone')
        cpf = request.POST.get('cpf')
        endereco = request.POST.get('endereco')
        estadoCivil = request.POST.get('estadoCivil')
        renda = request.POST.get('renda')
        profissao = request.POST.get('profissao')

        cliente = Cliente(
            nomeCompleto = nomeCompleto,
            email = email,
            dataNascimento = dataNascimento,
            telefone = telefone,
            cpf = cpf,
            endereco = endereco,
            estadoCivil = estadoCivil,
            renda = renda,
            profissao = profissao
        )
        
        try:
            cliente.save()
            return redirect(reverse('clientes'))
        except:
            return HttpResponse('erro ao salvar')

def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, 'upd_cliente.html', {'cliente':cliente})


def upd_cliente(request,id):
    cliente = Cliente.objects.get(id=id)
 
    cliente.nomeCompleto = request.POST.get('nomeCompleto')
    cliente.email = request.POST.get('email')
    cliente.dataNascimento = request.POST.get('dataNascimento')
    cliente.telefone = request.POST.get('telefone')
    cliente.cpf = request.POST.get('cpf')
    cliente.endereco = request.POST.get('endereco')
    cliente.estadoCivil = request.POST.get('estadoCivil')
    cliente.renda = request.POST.get('renda')
    cliente.profissao = request.POST.get('profissao')

    try:
        cliente.save()
        return redirect(reverse('clientes'))
    except:
        return HttpResponse('erro ao atualizar cliente')
    