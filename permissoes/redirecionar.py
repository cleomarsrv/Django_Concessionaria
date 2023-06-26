from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages


class RedirectPermissionRequiredMixin(PermissionRequiredMixin):
    login_url = reverse_lazy('login')

    def handle_no_permission(self):
        referer = self.request.META.get('HTTP_REFERER')
        if referer:
            messages.error(self.request, f'usuário sem permissão de acesso, contate o gerente. Página solicitada {self.request.path}')
            return HttpResponseRedirect(referer)
        messages.error(self.request, 'usuário sem permissão de acesso a pagina solicitada, contate o gerente.')
        return redirect(reverse_lazy('index'))

def RedirectPermissionRequired(request, slugCarro=None):
    def referer(request, slugCarro=None):
        referer = request.META.get('HTTP_REFERER')
        if referer:
            messages.error(request, f'usuário sem permissão de acesso, contate o gerente. Página solicitada {request.path}')
            return HttpResponseRedirect(referer)
        messages.error(request, 'usuário sem permissão de acesso a pagina solicitada, contate o gerente.')
        return redirect(reverse_lazy('index'))
    return referer
