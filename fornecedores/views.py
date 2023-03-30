from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Fornecedor
from django.urls import reverse

def fornecedores(request):
    if request.method == "GET":
        fornecedores = Fornecedor.objects.all()
        return render(request, 'fornecedores.html', {'fornecedores':fornecedores})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        enderecoCompleto = request.POST.get('enderecoCompleto')
        cnpj = request.POST.get('cnpj')
        fornecedor = Fornecedor(
            nome = nome,
            cnpj = cnpj,
            email = email,
            telefone = telefone,
            enderecoCompleto = enderecoCompleto
        )
        try:
            fornecedor.save()
            return redirect(reverse('fornecedores'))
        except:
            return HttpResponse('erro ao salvar')

def editar_fornecedor(request, id):
    fornecedor = Fornecedor.objects.get(id=id)
    return render(request, 'upd_fornecedor.html', {'fornecedor':fornecedor})

def upd_fornecedor(request, id):
    nome = request.POST.get('nome')
    cnpj = request.POST.get('cnpj')
    email = request.POST.get('email')
    telefone = request.POST.get('telefone')
    enderecoCompleto =request.POST.get('enderecoCompleto')
    fornecedor = Fornecedor.objects.get(id=id)

    fornecedor.nome = nome
    fornecedor.cnpj = cnpj
    fornecedor.email = email
    fornecedor.telefone = telefone
    fornecedor.enderecoCompleto = enderecoCompleto

    try:
        fornecedor.save()
        return redirect(reverse('fornecedores'))
    except:
        return HttpResponse('erro ao salvar')