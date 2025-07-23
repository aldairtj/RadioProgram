from django.shortcuts import render
from django.http import HttpResponse

def Hola(request):
    return HttpResponse("Hola mundo...!")