from django.urls import path
from . import views

urlpatterns = [
    path('', views.vendas, name='vendas'),
    path('editar_venda/<int:id>', views.editar_venda, name='editar_venda'),
]