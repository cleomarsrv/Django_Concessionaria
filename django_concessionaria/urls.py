from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth import views

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

urlpatterns += [
    path('contas/', include('django.contrib.auth.urls')),
    path('contas/login/', views.LoginView.as_view(), name='login'),
    path('contas/logout/', views.LogoutView.as_view(), name='logout'),
    path('contas/senha_redefinir/', views.PasswordResetView.as_view(), name='password_reset'),
    path('contas/senha_redifinir/solicitado', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('contas/redefinir/uidb64/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('contas/redefinir/sucesso', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = 'permissoes.redirecionar.handler403'