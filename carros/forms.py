from django import forms
from .models import Versao

class VersaoModelForm(forms.ModelForm):
    
    class Meta:
        model = Versao
        fields = "__all__"
        exclude = ['estoque','slugVersao']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'placeholder':field})
            self.fields[field].widget.attrs.update({'style': 'margin-bottom:17px;'})
            self.fields['nome'].widget.attrs.update({'placeholder':'nome da nova versao'})