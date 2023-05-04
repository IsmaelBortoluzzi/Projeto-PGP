from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/', create_cliente, name='create-cliente'),
    path('list/', ListCliente.as_view(), name='list-cliente'),
    #  path('edit/<int:pk>', edit_order, name='edit-order'),
]