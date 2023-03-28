from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes, name='clientes'),
    path('editar_cliente/<int:id>', views.editar_cliente, name='editar_cliente'),
    path('upd_cliente/<int:id>', views.upd_cliente, name='upd_cliente'),
]