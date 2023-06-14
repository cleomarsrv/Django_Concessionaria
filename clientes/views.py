from typing import Any, Dict
from django.db import models
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from .models import Cliente
from .forms import ClientModelForm
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin

class ClienteCreate(CreateView,LoginRequiredMixin):
    model = Cliente
    fields = '__all__'
    template_name = 'clientes/clientes.html'
    permisson_required = 'permissao_gerente'
    success_url = reverse_lazy('clientes:clientes')

    def get_context_data(self, **kwargs):
        context = super(ClienteCreate, self).get_context_data(**kwargs)
        context['clientes'] = Cliente.objects.all()
        return context

    def form_valid(self, form):
        messages.success(self.request, 'cliente cadastrado com sucesso.')
        return super().form_valid(form)