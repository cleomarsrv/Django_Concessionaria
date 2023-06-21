from django import forms
from .models import Colaborador

class ColaboradorModelForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields['dataDesligamento'].widget.attrs.update({'placeholder':'( opcional )'})