from django.shortcuts import render, redirect
from django.http import HttpResponse
from carros.models import Carro, Versao
from .models import Compra
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ComprasModelForm


class ComprasListar(ListView):
    model = Compra
    template_name = 'compras/compras.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['versoes'] = Versao.objects.all().order_by('-estoque')
        return context

class CompraCriar(CreateView, LoginRequiredMixin):
    model = Compra
    form_class = ComprasModelForm
    template_name = 'compras/compraForm.html'
    success_url = reverse_lazy('compras:listar')
    permission_required = 'compras.permissao_gerente', 'compras.permissao_supervisor'

    def form_valid(self, form):
        messages.success(self.request, 'compra lancada com sucesso. ')
        versaoCompra = form.cleaned_data.get('versao')
        quantidade = form.cleaned_data.get('quantidade')
        versao = Versao.objects.get(id=versaoCompra.id)
        versao.estoque += quantidade
        versao.save()
        return super().form_valid(form)

class CompraEditar(UpdateView):
    model = Compra
    form_class = ComprasModelForm
    template_name = 'compras/compraForm.html'
    success_url = reverse_lazy('compras:listar')

    def form_valid(self, form):
        messages.success(self.request, 'compra alterada com sucesso.')
        quantidadeAposEditar = form.cleaned_data['quantidade']
        versaoAposEditar = form.cleaned_data['versao']
        quantidadeAntesEditar = self.quantidadeAntesEditar
        versaoAntesEditar = self.versaoAntesEditar

        if versaoAntesEditar == versaoAposEditar:
            versaoAntesEditar.estoque += quantidadeAposEditar - quantidadeAntesEditar
            versaoAntesEditar.save()
        else:
            versaoAntesEditar.estoque -= quantidadeAntesEditar
            versaoAposEditar.estoque += quantidadeAposEditar
            versaoAposEditar.save()
            versaoAntesEditar.save()
        
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        objeto = self.get_object()
        initial['dataHora'] = objeto.dataHora.strftime('%Y-%m-%dT%H:%M')
        self.versaoAntesEditar = objeto.versao
        self.quantidadeAntesEditar = objeto.quantidade
        return initial


class CompraExcluirLogica(DeleteView):
    model = Compra
    template_name = 'compras/compraExcluir.html'
    success_url = reverse_lazy('compras:listar')

    def form_valid(self, form):
        messages.success(self.request, 'compra excluida com sucesso.')
        compra = self.get_object()
        versao = Versao.objects.get(id=compra.versao.id)
        quantidade = compra.quantidade
        versao.estoque -= quantidade
        versao.save()
        return super().form_valid(form)
