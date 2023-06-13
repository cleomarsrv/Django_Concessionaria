from django.urls import path
from . import views

app_name='carros'
urlpatterns = [
    path('', views.carros, name='carros'),
    path('<slug:slugCarro>/cadastrar_versao',views.cadastrar_versao, name='cadastrar_versao'),
    path('<slug:slugCarro>', views.versoes, name='versoes'),

    path('editar_carro/<int:id>', views.editar_carro, name='editar_carro'),
    path('upd_carro/<int:id>', views.upd_carro, name='upd_carro'),
    path('<slug:slugCarro>/<int:pk>/detalhe', views.versaoDetalheView.as_view(), name='detalhe'),
]