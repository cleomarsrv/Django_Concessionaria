from django.urls import path
from . import views

urlpatterns = [
    path('', views.carros, name='carros'),
    path('editar_carro/<int:id>', views.editar_carro, name='editar_carro'),
    path('upd_carro/<int:id>', views.upd_carro, name='upd_carro'),
]