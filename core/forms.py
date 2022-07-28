from genericpath import exists
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Categoria, Vehiculo, Cliente
from django.forms import ValidationError


class VehiculoForm(forms.ModelForm):
 
    class Meta: 
        model= Vehiculo
        fields = ['patente', 'marca', 'modelo', 'categoria']
        labels ={
            'patente': 'Patente', 
            'marca': 'Marca', 
            'modelo': 'Modelo', 
            'categoria': 'Categoría',
        }
        widgets={
            'patente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese patente', 
                    'id': 'patente'
                }
            ), 
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese marca', 
                    'id': 'marca'
                }
            ), 
            'modelo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese modelo', 
                    'id': 'modelo'
                }
            ), 
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            )
        }
        def clean_patente(self):
            patente = self.cleaned_data.get("patente")

            if Vehiculo.objects.filter(patente=patente).exists():
                raise ValidationError("Esta patente ya existe")
                
            return patente

class ClienteForm(forms.ModelForm):

    class Meta: 
        model = Cliente
        fields = ['idCliente','nombreCliente','correoCliente','fonoCliente','direCliente']
        labels ={
            'idCliente': 'Id', 
            'nombreCliente': 'Nombre', 
            'correoCliente': 'Correo', 
            'fonoCliente': 'Telefono',
            'direCliente': 'Direccion',
        }
        widgets={
            'idCliente': forms.TextInput(
                attrs={
                    
                    'class': 'form-control', 
                    'placeholder': 'Ingrese un Id', 
                    'id': 'idCliente'
                }
            ), 
            'nombreCliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombreCliente'
                }
            ), 
            'correoCliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese correo', 
                    'id': 'correoCliente'
                }
            ), 
            'fonoCliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese telefono', 
                    'id': 'fonoCliente'
                }
            ), 
            'direCliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese direccion', 
                    'id': 'direCliente'
                }
            )
        }