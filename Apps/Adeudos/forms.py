from django import forms
from .models import Mes, Concepto, Adeudo

class AdeudoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Alumno'].widget.attrs['autofocus'] = True

    class Meta:
        model = Adeudo
        fields = {'Alumno', 'Mes', 'Concepto', 'Importe',}

        widgets = {
                'Alumno': forms.Select(attrs={
                    'class': 'form-control', }),
                'Mes': forms.Select(attrs={
                    'class': 'form-control', }),     
                'Concepto': forms.Select(attrs={
                    'class': 'form-control', }),
                'Importe': forms.NumberInput(attrs={
                    'placeholder': 'Cantidad de cobro...',
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

