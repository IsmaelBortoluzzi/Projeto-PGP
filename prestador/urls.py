from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/', create_prestador, name='create-prestador'),
    path('list/', ListPrestador.as_view(), name='list-prestador'),
    #  path('edit/<int:pk>', edit_order, name='edit-order'),
]