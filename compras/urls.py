from django.urls import path
from . import views


app_name = 'compras'
urlpatterns = [
    path('', views.compras, name='compras'),
]