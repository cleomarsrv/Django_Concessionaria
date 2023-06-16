from django.urls import path
from . import views

app_name='carros'
urlpatterns = [
    path('', views.carros, name='listar'),
    path('cadastrar/', views.carroCriar, name='criar'),
    path('editar/<slug:slugCarro>/', views.carroEditar.as_view(), name='editar'),
    path('excluir/<slug:slugCarro>/', views.carroExcluir.as_view(), name='excluir'),
    
]

urlpatterns += [
    path('<slug:slugCarro>/versao/cadastrar/',views.versaoCriar, name='versaoCriar'),
    path('<slug:slugCarro>', views.versoes, name='versoes'),
    path('<slug:slugCarro>/versao/<int:pk>/detalhe', views.versaoDetalheView.as_view(), name='versaoDetalhe'),
]