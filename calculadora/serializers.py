from rest_framework import serializers
from . models import Reto, Jugadores, Usuario, partidas, Pie


class PieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pie
        fields = ('id', 'user_name', 'puntaje')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'password')

class PartidasSerializer(serializers.ModelSerializer):
    class Meta:
        model = partidas
        fields = ('id', 'fecha', 'usuario', 'minutos_jugados', 'puntaje')


class RetoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reto
        fields = ('id','nombre','minutos_jugados')

class JugadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jugadores
        fields = ('id','grupo','num_lista')