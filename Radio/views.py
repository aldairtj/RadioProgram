from django.shortcuts import render
from django.http import HttpResponse

def Hola(request):
    return HttpResponse("Hola mundo...!")

def Saludar(request):
    return HttpResponse("<h1>Hola clase como estan?</h1>")

def Saludar2(request,nombre):
    return HttpResponse(f"<h1>Hola {nombre} como estan?</h1>")


def calcular(request):
    numero = 100*9
    return HttpResponse(f"<h2 style=\"background-color:#000\">El resultado es: {numero}</h2>")

def espar(request,numero):
    respuesta = ""
    if numero % 2 == 0:
        respuesta = f"<h1>El numero {numero} es PAR</h1>"
    else:
        respuesta = f"<h1>El numero {numero} es IMPAR</h1>"
    return HttpResponse(respuesta)


def home(request):
    return render(request,'templates/home.html')