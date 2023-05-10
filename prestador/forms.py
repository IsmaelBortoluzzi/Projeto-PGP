from django import forms

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

        if valor is None:
            self.cleaned_data['valor'] = 0.0
        if comissao is None:
            self.cleaned_data['comissao'] = 0.0

        return super().clean()

