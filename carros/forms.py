from django import forms
from .models import Versao

class FormVersao(forms.ModelForm):
    class Meta:
        model = Versao
        fields = "__all__"
        exclude = ['estoque','slugVersao']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'placeholder':field})