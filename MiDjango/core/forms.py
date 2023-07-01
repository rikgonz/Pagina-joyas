from django import forms
from django.forms import ModelForm
from .models import Producto

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields={'id_producto','nom_producto','precio','stock','tipo_producto'}
    
    widget = {
        'id_producto': forms.NumberInput(attrs={'class':'form-control'}),
        'nom_producto': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})),
        'precio': forms.NumberInput(attrs={'class':'form-control'}),
        'stock': forms.NumberInput(attrs={'class':'form-control'}),
        'tipo_producto': forms.Select(attrs={'class':'form-control'})
    }
