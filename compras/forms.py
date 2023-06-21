from compras.models import Compra
from django import forms

class ComprasModelForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'
        widgets = {'dataHora':forms.DateTimeInput(attrs={'type':'datetime-local'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})
            self.fields[field].widget.attrs.update({'placeholder':field})