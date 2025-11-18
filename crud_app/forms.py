#crud_app /forms.py
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'servicio', 'categoria', 'descripcion', 'precio', 'duracion_dias', 'tipo_pantalla', 'stock', 'imagen', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Netflix - Pantalla Original 30 Días'}),
            'servicio': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción adicional (opcional)'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio en COP'}),
            'duracion_dias': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 30, 60, 90'}),
            'tipo_pantalla': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Original, Premium, Estándar'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad disponible'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CheckoutForm(forms.Form):
    nombre = forms.CharField(label='Nombre Completo', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre completo'}))
    email = forms.EmailField(label='Correo Electrónico', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'tu@email.com'}))
    telefono = forms.CharField(label='Teléfono de contacto', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+57 300 123 4567'}))
    direccion = forms.CharField(label='Dirección de envío', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección completa'}))
    notas = forms.CharField(label='Notas adicionales', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Instrucciones especiales (opcional)'}))