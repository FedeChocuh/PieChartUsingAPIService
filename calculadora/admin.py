from django.contrib import admin
from .models import Reto,Jugadores, Usuario, partidas, Pie

###############################################
############  TAREA 3.3  ######################
###############################################

admin.site.register(Pie)

###############################################
############  TAREA 1.4 REST ##################
###############################################

admin.site.register(Usuario)
admin.site.register(partidas)

###############################################

# Register your models here.
admin.site.register(Reto)
admin.site.register(Jugadores)
