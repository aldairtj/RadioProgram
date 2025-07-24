from django.contrib import admin # type: ignore
from django.urls import path # type: ignore

from . import views
urlpatterns = [
    path('',views.Index, name = "index"),
    path('Principal',views.Principal, name = "Principal"),
    path('Noticias',views.Noticias, name = "Noticias"),
    path('Musicas',views.Musicas, name = "Musicas"),
    path('Programas',views.Programas, name = "Programas"),
    path('Programas/Byte a Byte',views.Prog1, name = "Prog1"),
    path('Programas/Zona Retro',views.Prog2, name = "Prog2"),
    path('Programas/Compilando Ideas',views.Prog3, name = "Prog3"),
    path('Programas/Play Digital',views.Prog4, name = "Prog4"),
    path('Programas/Mente y Código',views.Prog5, name = "Prog5"),
    path('Programas/Frecuencia Libre',views.Prog6, name = "Prog6"),
    path('Contacto', views.registrar_oyente, name="Contacto"),
]