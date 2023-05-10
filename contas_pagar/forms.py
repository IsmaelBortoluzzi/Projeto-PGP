from django import forms

from contas_pagar.models import ContasPagar

class ContasPagarForm(forms.ModelForm):
    
    STATUS_CHOICES = (
        ('A', 'Aberto'),
        ('P', 'Pago'),
    )

    def clean(self):
        demanda = self.cleaned_data.get('demanda')
        valor = self.cleaned_data.get('valor')
        ##data_criacao = self.cleaned_data.get('data_criacao')
        return super().clean()

    class Meta:
        model = ContasPagar
        fields = ('demanda', 'valor')
