from pyexpat import model
from re import T
from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de categoria')

    def __str__(self):
        return self.nombreCategoria


class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True, verbose_name='Patente')        
    marca = models.CharField(max_length=20, verbose_name='Marca')
    modelo = models.CharField(max_length=20, verbose_name='Modelo')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente


class Cliente(models.Model):
    idCliente = models.IntegerField(primary_key=True, verbose_name='Id Cliente')
    nombreCliente = models.CharField(max_length=50, verbose_name='Nombre de cliente')
    correoCliente = models.EmailField(max_length=254, verbose_name='Email del cliente')
    fonoCliente = models.CharField(max_length=9, verbose_name='Telefono cliente')
    direCliente = models.CharField(max_length=100, verbose_name='Direccion del cliente')

    def __str__(self):
        return self.nombreCliente