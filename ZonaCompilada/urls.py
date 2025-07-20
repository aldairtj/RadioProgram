from django.contrib import admin # type: ignore
from django.urls import include, path # type: ignore

from . import views
urlpatterns = [
    path('',views.Index, name = "index"),
    path('Principal',views.Principal, name = "Principal"),
    path('Noticias',views.Noticias, name = "Noticias"),
    path('Musicas',views.Musicas, name = "Musicas"),
    path('Programas',views.Programas, name = "Programas"),
    #path('Contacto',views.Contacto, name = "Contacto"),
    path('Contacto', views.registrar_oyente, name="Contacto"),
    path('saludar',views.saludar, name = "saludar"),
    path('saludarconnombre/<str:nombre>',views.saludarconnombre, name = "saludarconnombre"),
    path('html',views.llamarplantilla,name = "html"),
    path('saludarhtml/<str:nombre>',views.saludarConPlantilla,name = "HolaHtml")
]