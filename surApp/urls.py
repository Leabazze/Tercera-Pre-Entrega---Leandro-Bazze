from django.urls import path , include
from surApp.views import *

urlpatterns = [
    path('padre/', padre, name='Padre'), #se le asigan una nombre para que luego django pueda llamarla por este
    path('cancha/',cancha , name='Cancha'),
    path('cargarjugador/',cargarJugador, name='CargarJugador'),
    path('inicio/',inicio, name='Inicio'),
    path('rival/', rival, name='Rival'),
    path('buscar-rival/',buscarRival, name = 'BuscarRival'),
    path('ver-rival/',buscar, name='VerRival'),
    path('simular/',simular, name='Simular'),
    path('resultado/',resultado, name='Resultado'),
    path('cargar-dt/',cargar_tecnico, name='CargarDt')
]