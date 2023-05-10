from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

from contas_pagar.forms import ContasPagarForm
from contas_pagar.models import ContasPagar


def create_contas_pagar(request):
    if request.method == 'GET':
        context = {
            'contas_pagar_form': ContasPagarForm(),
        }
        return render(request, 'contas_pagar/create_contas_pagar.html', context)

    if request.method == 'POST':
        contas_pagar_form = ContasPagarForm(request.POST)

        if contas_pagar_form.is_valid():
            new_contas_pagar = contas_pagar_form.save(commit=False)
            new_contas_pagar.status = 'A'
            new_contas_pagar.save()

            messages.success(request, 'Salvo Com Sucesso!')
        else:
            messages.error(request, 'Não foi possível salvar a conta à pagar!')

        return HttpResponseRedirect(reverse('list-contas-pagar'))


class ListContasPagar(ListView):
    model = ContasPagar
    template_name = 'contas_pagar/list_contas_pagar.html'
    paginate_by = 15
    extra_context = dict()
    context_object_name = 'contas_pagar'

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.codigo = None

    def get_queryset(self):
        self.codigo = self.request.GET.get('codigo', None)
        return super().get_queryset()


def edit_contas_pagar(request, pk):

    if request.method == 'GET':
        context = {
            'contas_pagar_form': ContasPagarForm(instance=ContasPagar.objects.get(pk=pk))
        }
        return render(request, 'contas_pagar/edit_contas_pagar.html', context)

    if request.method == 'POST':
        contas_pagar_form = ContasPagarForm(request.POST)

        if contas_pagar_form.is_valid():
            updated_contas_pagar = contas_pagar_form.save(commit=False)
            updated_contas_pagar.id = pk
            updated_contas_pagar.data_criacao = ContasPagar.objects.get(pk=pk).data_criacao
            updated_contas_pagar.save(force_update=True)

            messages.success(request, 'Editado Com Sucesso!')

            return HttpResponseRedirect(reverse('list-contas-pagar'))

        else:
            messages.error(request, 'Erros nos dados!')
            return render(request, 'contas_pagar/edit_contas_pagar.html', {'contas_pagar_form': contas_pagar_form})
