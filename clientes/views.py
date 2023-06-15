from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .models import Cliente
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin

class ClienteCriar(CreateView,LoginRequiredMixin):
    model = Cliente
    fields = '__all__'
    template_name = 'clientes/cliente_criar.html'
    permisson_required = 'clientes.permissao_funcionario'
    success_url = reverse_lazy('clientes:listar')

    # def get_context_data(self, **kwargs):
    #     context = super(ClienteCriar, self).get_context_data(**kwargs)
    #     context['clientes'] = Cliente.objects.all()
    #     return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields:
            form.fields[field].widget.attrs.update({'class':'form-control'})
        return form

    def form_valid(self, form):
        messages.success(self.request, f'cliente {self.request.POST.get("nomeCompleto")} cadastrado com sucesso.')
        return super().form_valid(form)

class ClienteEditar(UpdateView, LoginRequiredMixin):
    model = Cliente
    fields = '__all__'
    template_name = 'clientes/cliente_editar.html'
    permission_required = 'clientes.permissao_funcionario'
    success_url = reverse_lazy('clientes:listar')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields:
            form.fields[field].widget.attrs.update({'class':'form-control'})
        return form

    def form_valid(self, form):
        messages.success(self.request, f'cliente {self.request.POST.get("nomeCompleto")} alterado com sucesso. ')
        return super().form_valid(form)

class ClienteListar(generic.ListView, LoginRequiredMixin):
    model = Cliente
    paginate_by = 8
    template_name = 'clientes/clientes.html'
    permission_required = 'clientes.permissao_funcionario'

class ClienteExcluir(generic.DeleteView, LoginRequiredMixin):
    model  = Cliente
    template_name = 'clientes/cliente_excluir.html'
    permission_required = 'clientes.permissao_gerente'
    success_url = reverse_lazy('clientes:listar')

    def form_valid(self, form):
        messages.success(self.request, 'Cliente excluido com sucesso.')
        return super().form_valid(form)