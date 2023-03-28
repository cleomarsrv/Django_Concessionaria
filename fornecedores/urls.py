from django.urls import path
from . import views

urlpatterns = [
    path('', views.fornecedores, name='fornecedores'),
    path('marcas/', views.marcas, name='marcas'),
    path('editar_fornecedor/<int:id>', views.editar_fornecedor, name='editar_fornecedor'),
    path('upd_fornecedor/<int:id>', views.upd_fornecedor, name='upd_fornecedor'),
]