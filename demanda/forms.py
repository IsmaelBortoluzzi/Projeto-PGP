from django import forms

from demanda.models import Demanda

class DemandaForm(forms.ModelForm):

    def clean(self):
        descricao = self.cleaned_data.get('descricao')
        quantidade_horas = self.cleaned_data.get('quantidade_horas')
        cliente = self.cleaned_data.get('cliente')
        return super().clean()
    
    class Meta:
        model = Demanda
        fields = ('cliente', 'descricao', 'quantidade_horas')