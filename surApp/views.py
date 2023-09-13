from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import *
from random import randrange

# Create your views here.
def inicio(req):
    return render (req, 'surApp/inicio.html')

def padre (req):
    lista = [7,9,10,5]
    return render (req, 'surApp/padre.html',{'notas':lista})


def cargarJugador(req:HttpRequest):
    if req.method =='POST':
        nombre = req.POST.get('nombre')
        apellido = req.POST.get('apellido')
        posicion = req.POST.get('posicion')
        
        jugador = Jugador.objects.filter(posicion=posicion)
        if jugador:
            return render(req, 'surApp/error.html')

        miJugador = Jugador(nombre=nombre, apellido=apellido, posicion=posicion)
        miJugador.save()

        return render(req,'surApp/inicio.html', {'jugador': jugador})
    else:
        posiciones=Posicion.choices
        posiciones_cargadas = []
        for posicion in posiciones:
            if Jugador.objects.filter(posicion=posicion[0]).exists():
                posiciones_cargadas.append(posicion[0])

    return render(req, 'surApp/cargarjugador.html', {'posiciones':posiciones, 'posiciones_cargadas':posiciones_cargadas})
    

def equipo(req):
    return render(req, 'equipo.html')

def cancha(req):
    tecnico = Tecnico.objects.last()
    lista = Jugador.objects.all()
    return render(req, 'surApp/cancha.html', {'lista':lista, 'tecnico':tecnico})

def rival(req):
    if req.method == 'POST':
        nombre = req.POST.get('nombre')
        puntaje = req.POST.get('puntaje')
        rival = Rival.objects.filter(nombre=nombre).first()
        if rival:
            return render(req, 'surApp/error.html')
        rival = Rival(nombre=nombre, puntaje=puntaje)
        rival.save()

        return render (req, 'surApp/rival.html', {'rival':rival})
    else:
        return render (req,'surApp/rival.html')
    
def buscarRival(req):

    return render (req, 'surApp/buscarRival.html')


def buscar(req):
    if req.GET['nombre']:
        nombre= req.GET['nombre']
        rivales=Rival.objects.filter(nombre__icontains=nombre)
        return render(req, 'surApp/ver-rival.html', {'rivales':rivales})
    else:
        return render(req, 'surApp/error.html')
    
def simular(req):
    rivales=Rival.objects.all
    return render (req, 'surApp/simular.html', {'rivales':rivales})

def resultado(req):
    if req.POST.get('rivales',None):
        nombre=req.POST['rivales']
        rival=Rival.objects.get(nombre=nombre)
        puntaje=rival.puntaje
        resultado_rival = randrange(0,puntaje)
        resultado_mio = randrange(0,6)
        if resultado_mio > resultado_rival:
            resultado = 'GANASTE'
        elif resultado_mio == resultado_rival:
            resultado = 'EMPATE'
        else:
            resultado= 'PERDISTE'
        return render (req, 'surApp/resultado.html', { 'resultado':resultado, 'resultado_mio':resultado_mio, 'resultado_rival':resultado_rival, 'rival':rival} )
    
    return render(req, 'surApp/inicio.html')
    
def cargar_tecnico (req):
    if req.method =='POST':
        nombre = req.POST.get('nombre')
        apellido = req.POST.get('apellido')
        edad = req.POST.get('edad')
        tecnico= Tecnico(nombre=nombre, apellido=apellido, edad= edad)
        tecnico.save()
        frase='carga exitosa'
        return render (req, 'surApp/exito-dt.html', {'tecnico':tecnico, 'frase':frase})
    else:
        return render (req, 'surApp/cargar-dt.html')
