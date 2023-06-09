from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/', create_demanda, name='create-demanda'),
    path('list/', ListDemanda.as_view(), name='list-demanda'),
    path('edit/<int:pk>', edit_demanda, name='edit-demanda'),
    path('delete/<int:pk>', delete_demanda, name='delete-demanda'),
    path('assumir/<int:demanda_pk>', assumir_demanda, name='assumir-demanda'),
]