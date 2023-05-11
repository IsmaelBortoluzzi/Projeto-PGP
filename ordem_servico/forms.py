from django import forms

from ordem_servico.models import OrdemServico


class OrdemServicoForm(forms.ModelForm):
    
    PROCESSO_CHOICES = (
        ('ORC', 'Orçamento'),
        ('DEV', 'Desenvolvimento'),
        ('PAG', 'Pagamento'),
    )
    processo = forms.ChoiceField(choices=PROCESSO_CHOICES)

    STATUS_CHOICES = (
        ('ABE', 'Aberta'),
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
