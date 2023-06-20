from django.urls import path
from . import views



app_name = 'colaboradores'
urlpatterns = [
    path('', views.ColaboradoresListar.as_view(), name='listar'),
    path('cadastrar/', views.ColaboradorCriar.as_view(), name='criar'),
    path('<int:pk>/detalhe', views.ColaboradorDetalhe.as_view(), name='detalhe'),
    path('<int:pk>/editar', views.ColaboradorEditar.as_view(), name='editar'),
    path('<int:pk>/excluir', views.ColaboradorExcluir.as_view(), name='excluir'),
]