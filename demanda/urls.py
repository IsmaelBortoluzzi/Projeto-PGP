from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/', create_demanda, name='create-demanda'),
    path('list/', ListDemanda.as_view(), name='list-demanda'),
    #  path('edit/<int:pk>', edit_order, name='edit-order'),
]