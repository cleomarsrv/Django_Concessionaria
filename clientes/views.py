from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .models import Cliente
from vendas.models import Venda
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import ClienteModelForm
from permissoes.redirecionar import RedirectPermissionRequiredMixin


class ClienteCriar(RedirectPermissionRequiredMixin, CreateView):
    form_class = ClienteModelForm
    template_name = 'clientes/clienteForm.html'
    success_url = reverse_lazy('clientes:listar')
    permission_required = 'clientes.permissao_funcionario'

    def form_valid(self, form):
        messages.success(self.request, f'cliente {self.request.POST.get("nomeCompleto")} cadastrado com sucesso.')
        return self.form_valid(form)
        
    def get_context_data(self, form=None):
        context = super().get_context_data()
        context['botaoNome'] = 'Cadastrar'
        return context

class ClienteListar(RedirectPermissionRequiredMixin, generic.ListView):
    model = Cliente
    paginate_by = 8
    template_name = 'clientes/clientes.html'
    permission_required = 'clientes.permissao_funcionario'

class ClienteDetalhe(RedirectPermissionRequiredMixin, generic.DetailView):
    model = Cliente
    template_name = 'clientes/clienteDetalhe.html'
    permission_required = 'clientes.permissao_funcionario'

class ClienteEditar(RedirectPermissionRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteModelForm
    template_name = 'clientes/clienteForm.html'
    permission_required = 'clientes.permissao_funcionario'
    success_url = reverse_lazy('clientes:listar')

    def form_valid(self, form):
        cpf =  form.cleaned_data['cpf']
        if (len(cpf) != 11) or (not cpf.isnumeric()):
            form.add_error('cpf', 'cpf deve ter 11 numeros, sem ponto, hifen, etc')
            return self.form_invalid(form)
        else:
            messages.success(self.request, f'cliente {self.request.POST.get("nomeCompleto")} alterado com sucesso. ')
            return super().form_valid(form)
    
    def get_context_data(self, form=None):
        context = super().get_context_data()
        context['botaoNome'] = 'Alterar'
        return context

class ClienteExcluir(RedirectPermissionRequiredMixin, generic.DeleteView):
    model  = Cliente
    template_name = 'clientes/clienteExcluir.html'
    permission_required = 'clientes.permissao_supervisor'
    success_url = reverse_lazy('clientes:listar')

    def form_valid(self, form):
        self.object = self.get_object()
        if Venda.objects.filter(cliente=self.object).exists():
            messages.error(self.request, f'{self.object.nomeCompleto}: existe venda para este cliente, nao pode ser excluído.')
            return redirect(reverse('clientes:listar'))
        messages.success(self.request, f'{self.object.nomeCompleto}: Cliente excluido com sucesso.')
        return super().form_valid(form)
