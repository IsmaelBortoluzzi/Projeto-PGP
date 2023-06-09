from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

from demanda.forms import DemandaForm
from demanda.models import Demanda
from ordem_servico.models import OrdemServico
from prestador.models import Prestador


def create_demanda(request):
    if request.method == 'GET':
        context = {
            'demanda_form': DemandaForm(),
        }
        return render(request, 'demanda/create_demanda.html', context)
    
    if request.method == 'POST':
        demanda_form = DemandaForm(request.POST)

        if demanda_form.is_valid():
            new_demanda = demanda_form.save()

            messages.success(request, 'Salvo Com Sucesso!')
        else:
            messages.error(request, 'Não foi possível salvar a demanda!')

        return HttpResponseRedirect(reverse('list-demanda'))

def edit_demanda(request, pk):
    if request.method == 'GET':
        demanda = Demanda.objects.get(pk=pk)
        context = {
            'demanda_form': DemandaForm(instance=demanda),
        }
        return render(request, 'demanda/edit_demanda.html', context)
    
    if request.method == 'POST':
        demanda = Demanda.objects.get(pk=pk)
        demanda_form = DemandaForm(request.POST, instance=demanda)

        if demanda_form.is_valid():
            demanda_form.save()

            messages.success(request, 'Salvo Com Sucesso!')
        else:
            messages.error(request, 'Não foi possível salvar a demanda!')

        return HttpResponseRedirect(reverse('list-demanda'))
    
def delete_demanda(request, pk):
    if request.method == 'GET':
        Demanda.objects.filter(pk=pk).delete()
        messages.success(request, 'Deletado Com Sucesso!')
        return HttpResponseRedirect(reverse('list-demanda'))

class ListDemanda(ListView):
    model = Demanda
    template_name = 'demanda/list_demanda.html'
    paginate_by = 15
    extra_context = dict()
    context_object_name = 'demandas'

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.codigo = None

    def get_queryset(self):
        self.codigo = self.request.GET.get('codigo', None)
        return super().get_queryset()


def assumir_demanda(request, demanda_pk):
    if request.method != 'GET':
        return HttpResponseRedirect(reverse('list-demanda'))
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('list-demanda'))

    demanda = Demanda.objects.get(pk=demanda_pk)

    OrdemServico.objects.create(
        demanda=demanda,
        processo='ORC',  # Orçamento
        status='ASS'  # Assumida
    )

    demanda.prestador = Prestador.objects.get(user=request.user)
    demanda.save()

    return HttpResponseRedirect(reverse('list-demanda'))