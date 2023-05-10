from django import forms

from contas_pagar.models import ContasPagar

class ContasPagarForm(forms.ModelForm):
    
    def __init__(self):
        super().__init__()
    
    STATUS_CHOICES = (
        ('ABE', 'Aberta'),
        ('ASS', 'Assumida'),
        ('FIN', 'Finalizada'),
    )

    def clean(self):
        demanda = self.cleaned_data.get('demanda')
        valor = self.cleaned_data.get('valor')
        ##data_criacao = self.cleaned_data.get('data_criacao')
        return super().clean()

    class Meta:
        model = ContasPagar
        fields = ('demanda', 'valor')
