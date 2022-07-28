from importlib.abc import PathEntryFinder
from site import venv
from sqlite3 import DateFromTicks
from django.shortcuts import render, redirect
from .models import Vehiculo, Cliente
from .forms import VehiculoForm, ClienteForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def registrate(request):
    return render(request, 'registrate.html')    

def feriados(request):
    return render(request, 'feriados.html')

def mostrar(request):
    vehiculos = Vehiculo.objects.all() #similar al select

    datos = {
        'vehiculos' : vehiculos
    }

    return render(request, 'mostrar.html', datos)

def form_vehiculo(request):
    if request.method=='POST':
        vehiculo_form = VehiculoForm(request.POST)
        if vehiculo_form.is_valid():
            vehiculo_form.save()
            return redirect ('mostrar')
    else:
        vehiculo_form = VehiculoForm()
    return render(request, 'form_vehiculo.html', {'vehiculo_form': vehiculo_form})    

def form_modvehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente = id)
    datos = {
        'form': VehiculoForm(instance=vehiculo)

    }
    if request.method == 'POST':
        formulario = VehiculoForm(data = request.POST, instance = vehiculo)
        if formulario.is_valid():
            formulario.save()
            return redirect ('mostrar')
    return render (request, 'form_modvehiculo.html', datos)


def form_delvehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente = id)
    vehiculo.delete()
    return redirect ('mostrar')


def listarcliente(request):
    cliente = Cliente.objects.all()

    datos = {
        'cliente' : cliente
    }
    return render(request, 'cliente.html', datos)

def form_cliente(request):
    if request.method=='POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect ('cliente')
    else:
        cliente_form = ClienteForm()
    return render(request, 'form_cliente.html', {'cliente_form': cliente_form})  


def form_modcliente(request, id):
    cliente = Cliente.objects.get(idCliente=id)

    datos={
        'cliente_form': ClienteForm(instance=cliente)
    }
    if request.method == 'POST':
        formulario = ClienteForm(data = request.POST, instance = cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect ('cliente')
    return render(request, 'form_modcliente.html', datos)

def form_delcliente(request, id):
    cliente = Cliente.objects.get(idCliente = id)
    cliente.delete()
    return redirect ('cliente')
