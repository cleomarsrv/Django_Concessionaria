from django.urls import path
from . import views

app_name='carros'
urlpatterns = [
    path('', views.carros, name='listar'),
    path('cadastrar/', views.carroCriar, name='criar'),
    path('editar/<slug:slugCarro>/', views.CarroEditar.as_view(), name='editar'),
    path('excluir/<slug:slugCarro>/', views.CarroExcluir.as_view(), name='excluir'),
]

urlpatterns += [
    path('<slug:slugCarro>/versao/cadastrar/',views.versaoCriar, name='versaoCriar'),
    path('<slug:slugCarro>', views.versoes, name='versoes'),
    path('<slug:slugCarro>/versao/<int:pk>/detalhe', views.VersaoDetalheView.as_view(), name='versaoDetalhe'),
    path('<slug:slugCarro>/versao/<int:pk>/editar', views.VersaoEditar.as_view(), name='versaoEditar'),
    path('<slug:slugCarro>/versao/<int:pk>/excluir', views.VersaoExcluir.as_view(), name='versaoExcluir'),
]