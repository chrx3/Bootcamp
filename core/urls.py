from unicodedata import name
from django.urls import URLPattern, path
from .views import form_delvehiculo, form_vehiculo, home, registrate, mostrar,form_modvehiculo, listarcliente, form_cliente, form_modcliente, form_delcliente

urlpatterns=[
    path('',home, name="home"),
    path('registrate/', registrate, name="registrate"),
    path('mostrar/', mostrar, name="mostrar"),
    path('form_vehiculo/', form_vehiculo, name="form_vehiculo"),
    path('form_modvehiculo/<id>', form_modvehiculo, name="form_modvehiculo"),
    path('form_delvehiculo/<id>', form_delvehiculo, name="form_delvehiculo"),
    path('cliente/', listarcliente, name="cliente"),
    path('form_cliente/', form_cliente, name="form_cliente"),
    path('form_modcliente/<id>', form_modcliente, name="form_modcliente"),
    path('form_delcliente/<id>', form_delcliente, name="form_delcliente"),
]