from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='inicio'),
    path('pessoas/', include('pessoas.urls')),
    path('carros/', include('carros.urls')),
    path('clientes/', include('clientes.urls')),
    path('colaboradores/', include('colaboradores.urls')),
    path('vendas/', include('vendas.urls')),
    path('compras/', include('compras.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = 'permissoes.redirecionar.handler403'