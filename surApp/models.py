from django.db import models
from django.db.models import IntegerChoices,IntegerField
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Posicion(models.IntegerChoices):
        ARQUERO = 1, ('Arquero')
        DEFENSOR_CENTRAL = 2, ('Central')
        LATERAL_IZ = 3, ('Lateral_izq')
        DEFENSOR_DER = 4, ('Lateral_der')
        MEDIOCAMPISTA_CENTRAL = 5, ('Mediocentro')
        DEFENSOR = 6, ('Defensor')
        WING_DERECHO = 7, ('wing_derecho')
        MEDIOCAMPISTA = 8, ('Mediocampista')
        DELANTERO_CENTRO = 9,('Delantero')
        ENGANCHE = 10, ('Enganche')
        DELANTERO = 11,('wing_izquierdo')

class Jugador(models.Model):
        nombre = models.CharField(max_length=40)
        apellido = models.CharField(max_length=40)
        posicion = models.IntegerField(choices = Posicion.choices ,unique=True)


class Rival(models.Model):
        nombre= models.CharField(max_length=40, unique=True)
        puntaje= models.IntegerField()
        
        def __str__(self) -> str:
                return f'{self.nombre}-{self.puntaje}'

class Tecnico (models.Model):
        nombre=models.CharField(max_length=40)
        apellido=models.CharField(max_length=40)
        edad= models.IntegerField()

        def __str__(self) -> str:
                return f'{self.nombre} {self.apellido} {self.edad}'