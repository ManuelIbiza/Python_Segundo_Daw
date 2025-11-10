from django.shortcuts import render
from django.http import HttpResponse

def base(request):
    return render(request, 'app1/base.html')

def inicio(request):
    return HttpResponse("¡Hola, esto es un blog!")
