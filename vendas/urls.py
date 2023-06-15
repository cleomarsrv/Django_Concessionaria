from django.urls import path
from . import views


app_name = 'vendas'
urlpatterns = [
    path('', views.vendas, name='vendas'),
    path('editar/<int:id>', views.editar, name='editar'),
]