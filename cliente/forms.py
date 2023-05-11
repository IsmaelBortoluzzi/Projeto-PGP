from django import forms

from cliente.models import Cliente


class ClienteForm(forms.ModelForm):
    
    def clean(self):
        nome = self.cleaned_data.get('nome')
        documento = self.cleaned_data.get('documento')
        telefone = self.cleaned_data.get('telefone')
        email = self.cleaned_data.get('email')
        return super().clean()

    class Meta:
        model = Cliente
        fields = ('nome','documento','telefone','email')
