from django import forms

from ordem_servico.models import OrdemServico


class OrdemServicoForm(forms.ModelForm):
    
    PROCESSO_CHOICES = (
        ('ORC', 'Orçamento'),
        ('FAT', 'Faturamento'),
        ('DEV', 'Desenvolvimento'),
        ('PAG', 'Pagamento'),
        ('FIN', 'Finalizado')
    )
    processo = forms.ChoiceField(choices=PROCESSO_CHOICES)

    STATUS_CHOICES = (
        ('ASS', 'Assumida'),
        ('FIN', 'Finalizada'),
    )

    def clean(self):
        demanda = self.cleaned_data.get('demanda')
        processo = self.cleaned_data.get('processo')
        return super().clean()

    class Meta:
        model = OrdemServico
        fields = ('demanda', 'processo')
