from django.urls import path, include
from . import views

app_name = 'pessoas'
urlpatterns = [
    path('add_pessoa/', views.add_pessoa, name='add_pessoa'),
    path('editar_pessoa/<int:id>', views.editar_pessoa, name='editar_pessoa'),
    path('upd_pessoa/<int:id>', views.upd_pessoa, name='upd_pessoa'),
]