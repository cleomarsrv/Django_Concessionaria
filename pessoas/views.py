from django.shortcuts import render, redirect, get_object_or_404
from .forms import PessoaForm
from .models import Pessoa
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
import json

def add_pessoa(request):
    if request.method == "GET":
        pessoas = Pessoa.objects.all()
        form = PessoaForm()
        return render(request, 'add_pessoa.html', {'form':form, 'pessoas':pessoas})
    elif request.method == "POST":
        nomeCompleto = request.POST.get('nomeCompleto')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        pessoa = Pessoa(
            nomeCompleto = nomeCompleto,
            email = email,
            cpf = cpf,
        )
        try:
            pessoa.save()
            return redirect(reverse('add_pessoa'))
        except:
            return HttpResponse('erro ao salvar')

def editar_pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, 'upd_pessoa.html', {'pessoa':pessoa})

def upd_pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    nomeCompleto = request.POST.get('nomeCompleto')
    email = request.POST.get('email')
    cpf = request.POST.get('cpf')
    pessoa.nomeCompleto = nomeCompleto
    pessoa.email = email
    pessoa.cpf = cpf
    pessoa.save()
    return redirect(add_pessoa)