from django.urls import path
from . import views


app_name = 'vendas'
urlpatterns = [
    path('', views.VendasListar.as_view(), name='listar'),
    path('cadastrar/', views.VendasCriar.as_view(), name='criar'),
    path('editar/<int:pk>', views.VendasEditar.as_view(), name='editar'),
    path('excluir/<int:pk>', views.VendasExcluir.as_view(), name='excluir'),
]