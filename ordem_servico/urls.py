from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/', create_ordem_servico, name='create-ordem-servico'),
    path('list/', ListOrdemServico.as_view(), name='list-ordem-servico'),
    #  path('edit/<int:pk>', edit_order, name='edit-order'),
]