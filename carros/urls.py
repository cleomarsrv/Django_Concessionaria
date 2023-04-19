from django.urls import path
from . import views

urlpatterns = [
    path('', views.carros, name='carros'),
    path('cadastrar_versao/<slug:slugCarro>',views.cadastrar_versao, name='cadastrar_versao'),
    path('<slug:slugCarro>', views.versoes, name='versoes'),

    path('editar_carro/<int:id>', views.editar_carro, name='editar_carro'),
    path('upd_carro/<int:id>', views.upd_carro, name='upd_carro'),
    # path('<slug:slugCarro>', views.carros_versoes, name='carros_versoes'),
]