from django.urls import path
from . import views

urlpatterns = [
    path('', views.carros, name='carros'),
    path('editar_carro/<int:id>', views.editar_carro, name='editar_carro'),
    path('upd_carro/<int:id>', views.upd_carro, name='upd_carro'),
    path('cadastrar_versao/<int:id>',views.cadastrar_versao, name='cadastrar_versao'),
    path('versoes/<slug:slugVersao>', views.versoes, name='versoes'),
    path('<slug:slugCarro>', views.carros, name='carros'),
]