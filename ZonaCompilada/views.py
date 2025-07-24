import feedparser
import os
from django.conf import settings
from django.http import HttpResponse # type: ignore
from django.shortcuts import render # type: ignore
from . import forms
from .models import Oyente

# Create your views here.
def Index(request):
    return render(request, "Inicio.html")

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
    media_dir = os.path.join(settings.MEDIA_ROOT, 'musica')
    audio_files = [f for f in os.listdir(media_dir) if f.endswith('.mp3')]
    image_files = [f for f in os.listdir(media_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]

    canciones = []
    for audio in audio_files:
        nombre_base = os.path.splitext(audio)[0]
        for imagen in image_files:
            if os.path.splitext(imagen)[0] == nombre_base:
                canciones.append({
                    'titulo': nombre_base.replace('_', ' ').title(),
                    'audio': f'musica/{audio}',
                    'imagen': f'musica/{imagen}',
                })
                break

    return render(request, "Musicas.html", {
        "canciones": canciones
    })

def Programas(request):
    return render(request, "Programas.html")

def Prog1(request):
    return render(request, "Prog1.html")

def Prog2(request):
    return render(request, "Prog2.html")

def Prog3(request):
    return render(request, "Prog3.html")

def Prog4(request):
    return render(request, "Prog4.html")

def Prog5(request):
    return render(request, "Prog5.html")

def Prog6(request):
    return render(request, "Prog6.html")

def registrar_oyente(request):
    if request.method == "POST":
        formulario = forms.FormularioOyente(request.POST)
        if formulario.is_valid():
            formulario.save()
            return render(request, "Registrado.html")
    else:
        formulario = forms.FormularioOyente()

    oyentes = Oyente.objects.all()  # Obtener todos los oyentes registrados

    return render(request, "Contacto.html", {
        "formulario": formulario,
        "oyentes": oyentes
    })