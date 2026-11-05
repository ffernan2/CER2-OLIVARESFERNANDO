from django import forms
from .models import LugarPatrimonial

class LugarForm(forms.ModelForm):
    class Meta:
        model=LugarPatrimonial
        fields = ['nombre', 'descripcion', 'ubicacion', 'anio_construccion', 'imagen', 'categoria']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'anio_construccion': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.URLInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
        }
