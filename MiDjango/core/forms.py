from django import forms
from django.forms import ModelForm
from .models import Producto, Ciudad, Comuna, TipoProducto, Cliente, Venta, DetalleVenta


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields={'id_producto','nom_producto','precio','stock','tipo_producto', 'imagen'}
    
    widget = {
        'id_producto': forms.NumberInput(attrs={'class':'form-control'}),
        'nom_producto': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})),
        'precio': forms.NumberInput(attrs={'class':'form-control'}),
        'stock': forms.NumberInput(attrs={'class':'form-control'}),
        'tipo_producto': forms.Select(attrs={'class':'form-control'}),
        'imagen': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})),
    }

class CiudadForm(ModelForm):
    class Meta:
        model = Ciudad
        fields = ['id_ciudad', 'nom_ciudad']
    
    widgets = {
        'id_ciudad': forms.NumberInput(attrs={'class':'form-control'}),
        'nom_ciudad': forms.TextInput(attrs={'class': 'form-control'}),
    }

class ComunaForm(ModelForm):
    class Meta:
        model = Comuna
        fields = ['id_comuna', 'nom_comuna', 'ciudad']
    
    widgets = {
        'id_comuna': forms.NumberInput(attrs={'class':'form-control'}),
        'nom_comuna': forms.TextInput(attrs={'class': 'form-control'}),
        'ciudad': forms.Select(attrs={'class': 'form-control'}),
    }

class TipoProductoForm(ModelForm):
    class Meta:
        model = TipoProducto
        fields = ['id_tipo_pro', 'nomb_producto']
    
    widgets = {
        'id_tipo_pro': forms.NumberInput(attrs={'class':'form-control'}),
        'nomb_producto': forms.TextInput(attrs={'class': 'form-control'}),
    }

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['id_cli', 'nombre', 'apellido', 'rut', 'email', 'direccion', 'fono', 'comuna']
    
    widgets = {
        'id_cli': forms.NumberInput(attrs={'class':'form-control'}),
        'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        'apellido': forms.TextInput(attrs={'class': 'form-control'}),
        'rut': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        'fono': forms.NumberInput(attrs={'class': 'form-control'}),
        'comuna': forms.Select(attrs={'class': 'form-control'}),
    }

class VentaForm(ModelForm):
    class Meta:
        model = Venta
        fields = ['id_venta', 'fecha_boleta', 'total_boleta']
    
    widgets = {
        'id_venta': forms.NumberInput(attrs={'class':'form-control'}),
        'fecha_boleta': forms.DateInput(attrs={'class': 'form-control'}),
        'total_boleta': forms.NumberInput(attrs={'class': 'form-control'}),
    }

class DetalleVentaForm(ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['venta', 'cliente', 'producto', 'cantidad', 'precio']
    
    widgets = {
        'venta': forms.Select(attrs={'class': 'form-control'}),
        'cliente': forms.Select(attrs={'class': 'form-control'}),
        'producto': forms.Select(attrs={'class': 'form-control'}),
        'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        'precio': forms.NumberInput(attrs={'class': 'form-control'}),
    }