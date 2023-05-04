from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

from prestador.forms import PrestadorForm
from prestador.models import Prestador


def create_prestador(request):
    if request.method == 'GET':
        context = {
            'prestador_form': PrestadorForm(),
        }
        return render(request, 'prestador/create_prestador.html', context)

    if request.method == 'POST':
        prestador_form = PrestadorForm(request.POST)

        if prestador_form.is_valid():
            new_prestador = Prestador()
            new_prestador_user = User()

            new_prestador_user.username = prestador_form.cleaned_data.get('username')
            new_prestador_user.first_name = prestador_form.cleaned_data.get('first_name')
            new_prestador_user.last_name = prestador_form.cleaned_data.get('last_name')
            new_prestador_user.email = prestador_form.cleaned_data.get('email')
            new_prestador_user.set_password(prestador_form.cleaned_data.get('password'))
            new_prestador_user.save()

            new_prestador.user = new_prestador_user
            new_prestador.valor = prestador_form.cleaned_data.get('valor')
            new_prestador.documento = prestador_form.cleaned_data.get('documento')
            new_prestador.chave_pix = prestador_form.cleaned_data.get('chave_pix')
            new_prestador.comissao = prestador_form.cleaned_data.get('comissao')
            new_prestador.save()

            messages.success(request, 'Salvo Com Sucesso!')
        else:
            messages.error(request, 'Não foi possível salvar o prestador!')

        return HttpResponseRedirect(reverse('list-prestador'))


class ListPrestador(ListView):
    model = Prestador
    template_name = 'prestador/list_prestador.html'
    paginate_by = 15
    extra_context = dict()
    context_object_name = 'prestadores'

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.codigo = None

    def get_queryset(self):
        self.codigo = self.request.GET.get('codigo', None)
        return super().get_queryset()
