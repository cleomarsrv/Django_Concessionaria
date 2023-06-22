from django import forms
from .models import Cliente

class ClienteModelForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ['__all__']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})

    
