from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Colaborador

class ColaboradoresListar(ListView):
    model = Colaborador
    fields = '__all__'
    template_name = 'colaboradores/colaboradores.html'
    paginate_by = 8

class ColaboradorCriar(CreateView):
    model = Colaborador
    fields = '__all__'
    template_name = 'colaboradores/colaboradorForm.html'
    success_url = reverse_lazy('colaboradores:listar')

class ColaboradorDetalhe(DetailView):
    model = Colaborador
    template_name = 'colaboradores/colaboradorDetalhe.html'

class ColaboradorEditar(UpdateView):
    pass

class ColaboradorExcluir(DeleteView):
    pass