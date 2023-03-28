from django.urls import path
from . import views

urlpatterns = [
    path('', views.colaboradores, name='colaboradores'),
    path('editar_colaborador/<int:id>', views.editar_colaborador, name='editar_colaborador'),
    path('upd_colaborador/<int:id>', views.upd_colaborador, name='upd_colaborador'),
]