from django import forms
from .models import Mes, Concepto, Adeudo

class AdeudoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Importe'].widget.attrs['autofocus'] = True

    class Meta:
        model = Adeudo
        fields = '__all__'

        widgets = {
                'Importe': forms.NumberInput(attrs={
                    'placeholder': 'Cantidad de cobro...',
                    'class': 'form-control', }),
                'Concepto': forms.Select(attrs={
                    'class': 'form-control', }),
                'Mes': forms.Select(attrs={
                    'class': 'form-control', }),
                'Padre': forms.Select(attrs={
                    'class': 'form-control', }),            
            }    

class ConceptoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Concepto'].widget.attrs['autofocus'] = True

    class Meta:
        model = Adeudo
        fields = {'Concepto',}

        widgets = {
                'Concepto': forms.TextInput(attrs={
                    'placeholder': 'Añade un nuevo concepto de cobro...',
                    'class': 'form-control', }),
            }    

