from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Colaborador
from .forms import ColaboradorModelForm
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from permissoes.redirecionar import RedirectPermissionRequiredMixin


class ColaboradoresListar(RedirectPermissionRequiredMixin, ListView):
    model = Colaborador
    fields = '__all__'
    template_name = 'colaboradores/colaboradores.html'
    permission_required = 'clientes.permissao_supervisor'
    paginate_by = 8


class ColaboradorCriar(RedirectPermissionRequiredMixin, CreateView):
    model = Colaborador
    form_class = ColaboradorModelForm
    template_name = 'colaboradores/colaboradorForm.html'
    permission_required = 'clientes.permissao_gerente'
    success_url = reverse_lazy('colaboradores:listar')

    def get_context_data(self):
        context = super().get_context_data()
        context['botaoNome'] = 'Cadastrar'
        return context

    def form_valid(self, form):
        nomeCompleto = form.cleaned_data['nomeCompleto']
        messages.success(self.request, f'Colaborador: {nomeCompleto } cadastrado com sucesso.')
        return super().form_valid(form)

class ColaboradorDetalhe(RedirectPermissionRequiredMixin, DetailView):
    model = Colaborador
    template_name = 'colaboradores/colaboradorDetalhe.html'
    permission_required = 'clientes.permissao_supervisor'

class ColaboradorEditar(RedirectPermissionRequiredMixin, UpdateView):
    model = Colaborador
    form_class = ColaboradorModelForm
    template_name = 'colaboradores/colaboradorForm.html'
    permission_required = 'clientes.permissao_gerente'
    success_url = reverse_lazy('colaboradores:listar')

    def get_context_data(self):
        context = super().get_context_data()
        context['botaoNome'] = 'Alterar'
        return context

    def form_valid(self, form):
        messages.success(self.request, f'Colaborador: {self.object.nomeCompleto } alterado com sucesso.')
        return super().form_valid(form)

@login_required(login_url=reverse_lazy('login'))
@permission_required('colaboradores.permissao_gerente', raise_exception=True)
def ColaboradorInativar(request, id):
    if request.method == 'GET':
        colaborador = get_object_or_404(Colaborador, id=id)
        acao = 'inativar'
        acaoBotao = 'danger'
        context = {
            'colaborador':colaborador,
            'acao':acao,
            'acaoBotao':acaoBotao,
        }
        return render(request, 'colaboradores/colaboradorVinculo.html',context=context)
    if request.method == 'POST':
        colaborador = get_object_or_404(Colaborador,id=id)
        colaborador.situacaoVinculo = 'Inativo'
        colaborador.save()
        messages.info(request, f'colaborador {colaborador.nomeCompleto} foi INATIVADO.')
        return redirect(reverse('colaboradores:listar'))

@login_required(login_url=reverse_lazy('login'))
@permission_required('colaboradores.permissao_gerente', raise_exception=True)
def ColaboradorReativar(request, id):
    if request.method == 'GET':
        colaborador = get_object_or_404(Colaborador, id=id)
        acao = 'reativar'
        acaoBotao = 'success'
        context = {
            'colaborador':colaborador,
            'acao':acao,
            'acaoBotao':acaoBotao,
            }
        return render(request, 'colaboradores/colaboradorVinculo.html',context=context)
    if request.method == 'POST':
        colaborador = get_object_or_404(Colaborador,id=id)
        colaborador.situacaoVinculo = 'Ativo'
        colaborador.save()
        messages.success(request, f'colaborador {colaborador.nomeCompleto} foi REATIVADO.')
        return redirect(reverse('colaboradores:listar'))
