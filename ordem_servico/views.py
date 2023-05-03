from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

from ordem_servico.forms import OrdemServicoForm
from ordem_servico.models import OrdemServico


def create_ordem_servico(request):
    if request.method == 'GET':
        context = {
            'ordem_servico_form': OrdemServicoForm(),
        }
        return render(request, 'ordem_servico/create_ordem_servico.html', context)

    if request.method == 'POST':
        order_form = OrdemServicoForm(request.POST)

        if order_form.is_valid():
            new_order = order_form.save()

            messages.success(request, 'Salvo Com Sucesso!')
        else:
            messages.error(request, 'Não foi possível salvar a ordem de serviço!')

        return HttpResponseRedirect(reverse('home'))


class ListOrdemServico(ListView):
    model = OrdemServico
    template_name = 'ordem_servico/list_ordem_servico.html'
    paginate_by = 15
    extra_context = dict()
    context_object_name = 'ordens'

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.codigo = None

    def get_queryset(self):
        self.codigo = self.request.GET.get('codigo', None)
        return super().get_queryset()