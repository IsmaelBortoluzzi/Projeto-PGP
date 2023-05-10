from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/', create_contas_pagar, name='create-contas-pagar'),
    path('list/', ListContasPagar.as_view(), name='list-contas-pagar'),
    # path('destroy/<int:pk>', destroy_contas_pagar, name='destroy-contas-pagar'),
]