from django import forms
from django.core.exceptions import ValidationError

from .models import Prestador


class PrestadorForm(forms.Form):
    username = forms.CharField(max_length=256, label='Username')
    first_name = forms.CharField(max_length=256, label='Nome')
    last_name = forms.CharField(max_length=256, label='Sobrenome')
    email = forms.EmailField(max_length=256)
    password = forms.CharField(max_length=256, label='Senha')
    valor = forms.DecimalField(required=False, decimal_places=2, max_digits=12)
    documento = forms.CharField(max_length=14)
    chave_pix = forms.CharField(max_length=255, required=False)
    comissao = forms.DecimalField(required=False, decimal_places=2, max_digits=12)

    def clean(self):
        valor = self.cleaned_data.get('valor')
        comissao = self.cleaned_data.get('comissao')
        username = self.cleaned_data.get('username')

        if valor is None:
            self.cleaned_data['valor'] = 0.0
        if comissao is None:
            self.cleaned_data['comissao'] = 0.0

        if Prestador.objects.filter(user__username=username).exists():
            raise ValidationError('username já existe')

        return super().clean()


class PrestadorEditForm(forms.Form):
    first_name = forms.CharField(max_length=256, label='Nome')
    last_name = forms.CharField(max_length=256, label='Sobrenome')
    email = forms.EmailField(max_length=256)
    password = forms.CharField(max_length=256, label='Senha', required=False)
    valor = forms.DecimalField(required=False, decimal_places=2, max_digits=12)
    documento = forms.CharField(max_length=14)
    chave_pix = forms.CharField(max_length=255, required=False)
    comissao = forms.DecimalField(required=False, decimal_places=2, max_digits=12)

    def clean(self):
        valor = self.cleaned_data.get('valor')
        comissao = self.cleaned_data.get('comissao')

        if valor is None:
            self.cleaned_data['valor'] = 0.0
        if comissao is None:
            self.cleaned_data['comissao'] = 0.0

        return super().clean()