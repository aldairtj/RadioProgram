import feedparser
from django.http import HttpResponse # type: ignore
from django.shortcuts import render # type: ignore
import datetime
from . import forms, models

# Create your views here.
def Index(request):
    return HttpResponse("Hola mundo desde clientes")

def Principal(request):
    return render(request, "Principal.html")

def Noticias(request):
    url = "https://rpp.pe/feed/"
    feed = feedparser.parse(url)

    # Debug: loguear bozo status y número de items
    print("RSS bozo:", feed.bozo, "Entries:", len(feed.entries))

    noticias = feed.entries[:16] if hasattr(feed, 'entries') else []
    return render(request, "Noticias.html", {"noticias": noticias})

def Musicas(request):
    return render(request, "Musicas.html")

def Programas(request):
    return render(request, "Programas.html")

def Contacto(request):
    return render(request, "Contacto.html")

def registrar_oyente(request):
    if request.method == "POST":
        formulario = forms.FormularioOyente(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponse("Te registraste correctamente como oyente de la radio.")
    else:
        formulario = forms.FormularioOyente()
    
    return render(request, "Contacto.html", {
        "formulario": formulario
    })
    
def saludar(request):
    return HttpResponse("<h1>Hola Miguel</h1>")

def saludarconnombre(request, nombre):
    return HttpResponse(f"<h1>Hola {nombre.capitalize()}</h1>")

def llamarplantilla(request):
    return render(request, "uno.html")

def saludarConPlantilla(request, nombre):
    fecha = datetime.datetime.now()
    return render(request, "dos.html", {
        "name":nombre.capitalize(),
        "fecha": fecha
    })