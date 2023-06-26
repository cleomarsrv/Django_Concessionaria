from .models import Carro, Versao, Seguranca, Direcao, Motor, Combustivel, Acessorio
from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from carros.forms import VersaoModelForm
from permissoes.redirecionar import RedirectPermissionRequiredMixin, RedirectPermissionRequired


@login_required(login_url=reverse_lazy('login'))
def carros(request):
    carros = Carro.objects.all()
    todasVersoes = Versao.objects.all()
    todasImagens = ""
    for todas in todasVersoes:
        todasImagens += todas.imagem.url + ","
    
    context = {
        'carros':carros,
        'todasImagens':todasImagens,
    }
    return render(request, 'carros/carros.html', context=context)

@login_required(login_url=reverse_lazy('login'))
@RedirectPermissionRequired
# @permission_required('carros.permissao_supervisor', login_url=reverse_lazy('index'))
@permission_required('carros.permissao_supervisor', raise_exception=True)
def carroCriar(request):
    if request.method == "GET":
        return render(request, 'carros/carroCriar.html')
    elif request.method == "POST":
        nome = request.POST.get("nome")
        carro = Carro ( nome= nome,)
        carro.save()
        messages.add_message(request, constants.SUCCESS, f'carro {nome} cadastrado com sucesso')
        messages.add_message(request, constants.INFO, 'cadastre agora uma versão:')
        slugCarro = carro.slugCarro
        return redirect(reverse('carros:versaoCriar', kwargs={'slugCarro':slugCarro}))
        
class CarroEditar(RedirectPermissionRequiredMixin, UpdateView):
    model = Carro
    fields = ['nome']
    template_name = 'carros/carroEditar.html'
    permission_required = 'carros.permissao_supervisor'
    # raise_exception = True
    
    success_url = reverse_lazy('carros:listar')

    def get_object(self, queryset=None):
        slug_field = 'slugCarro'
        slug = self.kwargs.get(slug_field)
        queryset = self.get_queryset()
        obj = queryset.get(**{slug_field: slug})
        return obj

class CarroExcluir(RedirectPermissionRequiredMixin, DeleteView):
    model = Carro
    template_name = 'carros/carroExcluir.html'
    permission_required = 'carros.permissao_gerente'
    success_url = reverse_lazy('carros:listar')

    def get_object(self, queryset=None):
        slug_field = 'slugCarro'
        slug = self.kwargs.get(slug_field)
        queryset = self.get_queryset()
        obj = queryset.get(**{slug_field: slug})
        return obj

    def form_valid(self, form):
            self.object = self.get_object()
            if Versao.objects.filter(carro=self.object).exists():
                messages.error(self.request,'este carro já tem versão cadastrada!' )
                return redirect(reverse('carros:versoes', kwargs={'slugCarro':self.object.slugCarro}))
            messages.success(self.request, f'carro {self.object.nome} excluido com sucesso')
            return super().form_valid(form)

@login_required(login_url=reverse_lazy('login'))
def versoes(request, slugCarro):
    carroSelecionado = Carro.objects.get(slugCarro=slugCarro)
    versoes = Versao.objects.filter(carro__id=carroSelecionado.id)

    context = {
        'versoes':versoes,
        'carroSelecionado':carroSelecionado,
    }
    return render(request, 'carros/carroVersoes.html', context=context)


class VersaoDetalheView(RedirectPermissionRequiredMixin, generic.DetailView):
    model = Versao
    template_name='carros/versaoDetalhe.html'
    permission_required = 'carros.permissao_funcionario'

@login_required(login_url=reverse_lazy('login'))
@RedirectPermissionRequired
@permission_required('carros.permissao_supervisor')
def versaoCriar(request, slugCarro):
    carro = Carro.objects.get(slugCarro=slugCarro)
    if request.method == "GET":
        form = VersaoModelForm()
        context = {
            'carro':carro,
            'form':form
        }
        return render(request, 'carros/versaoCriar.html', context=context)
    elif request.method == "POST":
        form = VersaoModelForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        messages.add_message(request, constants.SUCCESS, 'versão cadastrada com sucesso.')
    else:
        messages.add_message(request, constants.ERROR, form.errors)
        context = {
            'carro':carro,
            'form':form,
        }
        return render(request, 'carros/versaoCriar.html', context=context)

    slugCarro = carro.slugCarro
    return redirect(reverse('carros:versoes', kwargs={'slugCarro':slugCarro}))


class VersaoEditar(RedirectPermissionRequiredMixin, UpdateView):
    model = Versao
    fields = ['nome','motor','combustivel','direcao','seguranca','acessorio','imagem','ano','modelo']
    template_name = 'carros/versaoEditar.html'
    permission_required = 'carros.permissao_supervisor'
    # success_url = reverse_lazy('carros:listar')

    def get_success_url(self):
        versao_id = self.kwargs['pk']
        versao = Versao.objects.get(id=versao_id)
        carro = versao.carro
        slugCarro = carro.slugCarro
        return reverse_lazy ('carros:versaoDetalhe', kwargs={'slugCarro':slugCarro, 'pk':versao_id})
    
    def form_valid(self,form):
        messages.success(self.request, 'versao alterada com sucesso')
        return super().form_valid(form)

class VersaoExcluir(RedirectPermissionRequiredMixin, DeleteView):
    model = Versao
    template_name = 'carros/versaoExcluir.html'
    success_url = reverse_lazy('carros:versoes', kwargs={'slugCarro':'teste'})
    permission_required = 'carros.permissao_supervisor'

