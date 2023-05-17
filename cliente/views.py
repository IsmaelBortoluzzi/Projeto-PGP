from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

from cliente.forms import ClienteForm
from cliente.models import Cliente


def create_cliente(request):
    if request.method == 'GET':
        context = {
            'cliente_form': ClienteForm(),
        }
        return render(request, 'cliente/create_cliente.html', context)

    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)

        if cliente_form.is_valid():
            new_order = cliente_form.save()

            messages.success(request, 'Salvo Com Sucesso!')

            return HttpResponseRedirect(reverse('list-cliente'))
        else:
            messages.error(request, 'Não foi possível salvar o cliente!')
            return render(request, 'cliente/create_cliente.html', {'cliente_form': cliente_form})

        return HttpResponseRedirect(reverse('home'))


class ListCliente(ListView):
    model = Cliente
    template_name = 'cliente/list_cliente.html'
    paginate_by = 15
    extra_context = dict()
    context_object_name = 'clientes'

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.codigo = None

    def get_queryset(self):
        self.codigo = self.request.GET.get('codigo', None)
        return super().get_queryset()
    
    

def edit_cliente(request, pk):

    cliente = Cliente.objects.get(pk=pk)

    if request.method == 'GET':

        context = {
            'cliente_form': ClienteForm(instance=cliente)
        }
        return render(request, 'cliente/edit_cliente.html', context)

    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST, instance=cliente)

        if cliente_form.is_valid():

            cliente_form.save()

            messages.success(request, 'Editado Com Sucesso!')

            return HttpResponseRedirect(reverse('list-cliente'))

        else:
            messages.error(request, 'Erros nos dados!')
            return render(request, 'cliente/edit_cliente.html', {'cliente_form': cliente_form})

def delete_cliente(request, pk):
    if request.method == 'GET':
        Cliente.objects.filter(pk=pk).delete()
        messages.success(request, 'Deletado Com Sucesso!')
        return HttpResponseRedirect(reverse('list-cliente'))
