from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/', create_prestador, name='create-prestador'),
    path('list/', ListPrestador.as_view(), name='list-prestador'),
    path('edit/<int:pk>', edit_prestador, name='edit-prestador'),
    path('delete/<int:pk>', delete_prestador, name='delete-prestador'),
]