from django.urls import path
from . import views


app_name = 'fornecedores'
urlpatterns = [
    path('', views.fornecedores, name='fornecedores'),
    path('editar_fornecedor/<int:id>', views.editar_fornecedor, name='editar_fornecedor'),
    path('upd_fornecedor/<int:id>', views.upd_fornecedor, name='upd_fornecedor'),
]