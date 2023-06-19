from compras.models import Compra
from django import forms

class ComprasModelForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'
        widgets = {'dataHora':forms.DateTimeInput(attrs={'type':'datetime-local'})}

