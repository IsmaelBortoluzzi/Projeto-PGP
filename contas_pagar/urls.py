from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/', create_contas_pagar, name='create-contas-pagar'),
    path('list/', ListContasPagar.as_view(), name='list-contas-pagar'),
    #  path('edit/<int:pk>', edit_order, name='edit-contas-pagar'),
]