from django.urls import path
from . import views


app_name = 'clientes'
urlpatterns = [
    path('', views.ClienteListar.as_view(), name='listar'),
    path('cadastrar/', views.ClienteCriar.as_view(), name='criar'),
    path('editar/<int:pk>', views.ClienteEditar.as_view(), name='editar'),
    path('excluir/<int:pk>', views.ClienteExcluir.as_view(), name='excluir'),
    path('<int:pk>/detalhe', views.ClienteDetalhe.as_view(), name='detalhe'),
]
