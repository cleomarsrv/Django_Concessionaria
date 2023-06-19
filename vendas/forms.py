from django import forms
from .models import Venda

class VendasModelForm(forms.ModelForm):

    class Meta:
        model = Venda
        fields = '__all__'
        widgets = {'dataHora':forms.DateTimeInput(attrs={'type':'datetime-local'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})
            self.fields[field].widget.attrs.update({'placeholder':field})

