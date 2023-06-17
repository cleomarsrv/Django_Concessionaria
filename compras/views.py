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


class CompraCriar(CreateView, LoginRequiredMixin):
    model = Compra
    form_class = ComprasModelForm
    template_name = 'compras/compraForm.html'
    success_url = reverse_lazy('compras:listar')
    permission_required = 'compras.permissao_gerente', 'compras.permissao_supervisor'

    def form_valid(self, form):
        messages.success(self.request, 'compra lancada com sucesso. ')
        return super().form_valid(form)

class CompraEditar(UpdateView):
    model = Compra
    form_class = ComprasModelForm
    template_name = 'compras/compraForm.html'
    success_url = reverse_lazy('compras:listar')

    def form_valid(self, form):
        messages.success(self.request, 'compra alterada com sucesso.')
        return super().form_valid(form)


class ComprasListar(ListView):
    model = Compra
    template_name = 'compras/compras.html'
    paginate_by = 10


class CompraExcluirLogica(DeleteView):
    model = Compra
    template_name = 'compras/compraExcluir.html'
    success_url = reverse_lazy('compras:listar')

    def form_valid(self, form):
        messages.warning(self.request, 'compra excluida com sucesso.')
        return super().form_valid(form)

# def compras(request):
#     if request.method == "GET":
#         carros = Carro.objects.all()
#         versoes = Versao.objects.all()
#         compras = Compra.objects.all()
#         context = {
#             'carros':carros,
#             'versoes':versoes,
#             'compras':compras
#         }
#         return render(request, 'compras/compras.html', context=context)
#     elif request.method == "POST":
#         versao_id = request.POST.get('versao')
#         quantidade = request.POST.get('quantidade')

#         compra = Compra()
#         versao = Versao.objects.get(id=versao_id)
#         compra.dataHora = request.POST.get('dataHora')
#         compra.versao_id = versao_id
#         compra.quantidade = quantidade
#         compra.valorTotal = request.POST.get('valorTotal')
        
#         versao.estoque += int(quantidade)

#         try:
#             compra.save()
#             versao.save()
#             messages.add_message(request, messages.constants.SUCCESS, 'compra lançada com sucesso')
#             return redirect(reverse('compras:compras'))
#         except:
#             messages.add_message(request, messages.constants.ERROR, 'erro ao lançar a compra, tente novamente.')
#             return redirect(reverse('compras:compras'))
    