from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from ordem_servico.forms import OrdemServicoForm


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

        return HttpResponseRedirect(reverse('list-order'))
