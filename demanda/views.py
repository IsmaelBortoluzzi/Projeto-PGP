from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

from demanda.forms import DemandaForm
from demanda.models import Demanda

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

        return HttpResponseRedirect(reverse('home'))
    
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