from django.urls import path
from . import views


app_name = 'colaboradores'
urlpatterns = [
    path('', views.colaboradores, name='colaboradores'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('upd_colaborador/<int:id>', views.upd_colaborador, name='upd_colaborador'),
]