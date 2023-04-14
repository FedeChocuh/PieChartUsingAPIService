from django.db import models

class Pie(models.Model):
    user_name = models.CharField(max_length=20)
    puntaje = models.IntegerField()


class Usuario(models.Model):
    password = models.CharField(max_length=30)

class partidas(models.Model):
    fecha = models.CharField(max_length=30)
    usuario = models.ForeignKey(Usuario, related_name= "id_usuario", on_delete=models.CASCADE)
    minutos_jugados = models.IntegerField()
    puntaje = models.IntegerField()
    




# Create your models here.

class Reto(models.Model):
    nombre = models.CharField(max_length=30)
    minutos_jugados = models.IntegerField()

class Jugadores(models.Model):
    grupo = models.CharField(max_length=2)
    num_lista = models.IntegerField()