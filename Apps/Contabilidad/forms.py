from django import forms
from django.contrib.admin import widgets
from .models import Ingreso, Gasto, Cat_Gasto, Cat_Ingreso, year, Recibo
from Apps.Alumnos.models import Padre


class YearForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ano'].widget.attrs['autofocus'] = True

    class Meta:
        model = year
        fields= '__all__'

        widgets = {
            'ano': forms.SelectMultiple(),
        }    
    

class IngresoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['concepto'].widget.attrs['autofocus'] = True

    class Meta:
        model = Ingreso
        fields = '__all__'

        widgets = {
                'concepto': forms.TextInput(attrs={
                    'placeholder': 'Concepto de cobro...',
                    'class': 'form-control', }),
                'categoria': forms.Select(attrs={
                    'class': 'form-control', }),
                'fecha': forms.DateInput(attrs={
                    'class': 'form-control datepicker', }),
                'cantidad': forms.NumberInput(attrs={
                    'class': 'form-control', }),            
            }    

class GastoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['concepto'].widget.attrs['autofocus'] = True

    class Meta:
        model = Gasto
        fields = '__all__'

        widgets = {
                'concepto': forms.TextInput(attrs={
                    'placeholder': 'Concepto de cobro...',
                    'class': 'form-control', }),
                'categoria': forms.Select(attrs={
                    'class': 'form-control', }),
                'fecha': forms.DateInput(attrs={
                    'class': 'form-control datepicker', }),
                'cantidad': forms.NumberInput(attrs={
                    'class': 'form-control', }),            
            }    

class CatIngresoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].widget.attrs['autofocus'] = True

    class Meta:
        model = Cat_Ingreso
        fields = {'categoria',}

        widgets = {
                'Concepto': forms.TextInput(attrs={
                    'placeholder': 'Añade un nuevo concepto de ingreso...',
                    'class': 'form-control', }),
            }                

class CatGastoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].widget.attrs['autofocus'] = True

    class Meta:
        model = Cat_Gasto
        fields = {'categoria',}

        widgets = {
                'categoria': forms.TextInput(attrs={
                    'placeholder': 'Añade un nuevo concepto de gasto...',
                    'class': 'form-control', }),
            }    

class ReciboForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['padre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Recibo
        fields = '__all__'

        widgets = {
                'padre': forms.Select(attrs={
                    'class': 'form-control', }),
                'concepto': forms.TextInput(attrs={
                    'placeholder': 'Concepto de recibo...',
                    'class': 'form-control', }),       
                'fecha': forms.DateInput(attrs={
                    'class': 'datepicker form-control', }),
                'cantidad': forms.NumberInput(attrs={
                    'class': 'form-control', }),            
            }    
