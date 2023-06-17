from django.urls import path
from . import views


app_name = 'compras'
urlpatterns = [
    path('', views.ComprasListar.as_view(), name='listar'),
    path('cadastrar/', views.CompraCriar.as_view(), name='criar'),
    path('<int:pk>/editar', views.CompraEditar.as_view(), name='editar'),
    path('<int:pk>/excluir', views.CompraExcluirLogica.as_view(), name='excluir'),
]