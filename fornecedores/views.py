from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Marca, Fornecedor
from django.urls import reverse

def fornecedores(request):
    if request.method == "GET":
        marcas = Marca.objects.all()
        fornecedores = Fornecedor.objects.all()
        return render(request, 'fornecedores.html', {'marcas':marcas, 'fornecedores':fornecedores})
    elif request.method == "POST":
        nomeFornecedor = request.POST.get('nomeFornecedor')
        emailFornecedor = request.POST.get('emailFornecedor')
        enderecoFornecedor = request.POST.get('enderecoFornecedor')
        cnpjFornecedor = request.POST.get('cnpjFornecedor')
        marcaFornecida = request.POST.get('marcaFornecida')
        fornecedor = Fornecedor(
            nomeFornecedor = nomeFornecedor,
            cnpjFornecedor = cnpjFornecedor,
            marcaFornecida_id = marcaFornecida,
            emailFornecedor = emailFornecedor,
            enderecoFornecedor = enderecoFornecedor
        )
        try:
            fornecedor.save()
            return redirect(reverse('fornecedores'))
        except:
            return HttpResponse('erro ao salvar')

def editar_fornecedor(request, id):
    fornecedor = Fornecedor.objects.get(id=id)
    marcas = Marca.objects.all()
    return render(request, 'upd_fornecedor.html', {'fornecedor':fornecedor, 'marcas':marcas})

def upd_fornecedor(request, id):
    nomeFornecedor = request.POST.get('nomeFornecedor')
    cnpjFornecedor = request.POST.get('cnpjFornecedor')
    marcaFornecida_id = request.POST.get('marcaFornecida')
    emailFornecedor = request.POST.get('emailFornecedor')
    enderecoFornecedor =request.POST.get('enderecoFornecedor')
    fornecedor = Fornecedor.objects.get(id=id)

    fornecedor.nomeFornecedor = nomeFornecedor
    fornecedor.cnpjFornecedor = cnpjFornecedor
    fornecedor.marcaFornecida_id = marcaFornecida_id
    fornecedor.emailFornecedor = emailFornecedor
    fornecedor.enderecoFornecedor = enderecoFornecedor

    fornecedor.save()
    return redirect(fornecedores)

def marcas(request):
    if request.method == "GET":
        pass
    elif request.method  == "POST":
        marcas = Marca.objects.all()
        nomeMarca = request.POST.get('nomeMarca')
        cnpjMarca = request.POST.get('cnpjMarca')
        print(cnpjMarca)
                
        marca = Marca(
            nomeMarca = nomeMarca,
            cnpjMarca = cnpjMarca
        )
        try:
            marca.save()
            return render(request, 'fornecedores.html', {'marcas':marcas})
        except:
            return HttpResponse('erro ao salvar')



