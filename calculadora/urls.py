
from django.urls import include,path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'reto', views.RetoViewSet)
router.register(r'jugador', views.JugadoresViewSet)
router.register(r'usuario', views.UsuarioViewSet)
router.register(r'partidas', views.PartidasViewSet)
router.register(r'pie', views.PieViewSet)


urlpatterns = [
    path('api',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('',views.index, name='index'),
    path('procesamiento', views.procesamiento, name='procesamiento'),
    path('usuarios', views.usuarios, name='usuarios'),
    path('usuarios_p', views.usuarios_p, name='usuarios_p'),
    path('usuarios_d', views.usuarios_d, name="usuarios_d"),
    path('usuarios_u', views.usuarios_u, name='usuarios_u'),
    path('login', views.login, name='login'),
    path('barras', views.barras, name='barras'),
    path('grafica', views.grafica, name='grafica'),
    path('lista', views.lista, name='lista'),
    path('valida_usuario', views.valida_usuario, name='valida_usuario'),
    path('login2', views.login2, name='login2'),
    path('procesologin', views.procesologin, name='procesologin'),
    path('pie', views.pie, name='pie'),
]
