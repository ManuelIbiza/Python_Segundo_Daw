from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import pprint
import json
import os

# Create your views here.
def base(request):
    return render(request, 'app4_biblioteca/base.html')

def mostrar_uno(request):
    # Cargar el JSON desde la ruta absoluta del proyecto
    ruta_json = os.path.join(settings.BASE_DIR, 'app4_biblioteca', 'socios.json')
    with open(ruta_json, 'r', encoding='utf-8') as f:
        datos = json.load(f)

    socios = datos['socios']
    nombre = request.GET.get("lectores")

    # HTML base + estilos
    respuesta = '''
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f4; }
            h1 { text-align: center; }
            .carnet {
                width: 600px;
                margin: 20px auto;
                padding: 2%;
                background-color: rgb(0,0,0);
                padding: 5px;
                overflow: hidden;
            }
            .foto {
                float: left;
                width: 30%%;
                text-align: center;
            }
            .foto img {
                width: 200px;
                heigth: 300px;
                border-radius: 10px;
                border: solid #fff 2px;
            }
            .datos {
                text-align:center;
                float: right;
                background-color: rgb(255,255,255);
                width: 60%;
                heigth: 90%;
                padding: 5px;
            }
            .dato {
                display: block;
                margin: 15px 0;
                color: #333;
                font-weight: bold;
            }
            #btn {
                display: block;
                margin: 20px auto;
            }
            a{
            text-decoration: none;
            }

        </style>
    </head>
    <body>
        <h1>Carnet solicitado:</h1>
        <br>
        <div>
    '''

    for socio in socios:
        if socio["nombre_apellidos"] == nombre:
            carnet = f'''
            <div class="carnet">
                <div class="foto">
                    <img src="{socio["foto"]}" alt="imagen_{socio["numero_carnet"]}">
                </div>
                <div class="datos">
                    <span class="dato">{socio["nombre_apellidos"]}</span>
                    <br>
                    <span class="dato">{socio["fecha_nacimiento"]}</span>
                    <br>
                    <span class="dato">{socio["numero_carnet"]}</span>
                </div>
            </div>
            '''
            respuesta += carnet

    respuesta += '''</div>
            <a href="http://127.0.0.1:8000/app4_biblioteca/base/">
                <button id="btn">Ir a la página base</button>
            </a>
        </body></html>'''
    
    return HttpResponse(respuesta)

def mostrar_todos(request):
    # Cargar el JSON desde la ruta absoluta del proyecto
    ruta_json = os.path.join(settings.BASE_DIR, 'app4_biblioteca', 'socios.json')
    with open(ruta_json, 'r', encoding='utf-8') as f:
        datos = json.load(f)

    socios = datos['socios']

    # HTML base + estilos
    respuesta = '''
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f4; }
            h1 { text-align: center; }
            .carnet {
                width: 600px;
                margin: 20px auto;
                padding: 2%;
                background-color: rgb(0,0,0);
                padding: 5px;
                overflow: hidden;
            }
            .foto {
                float: left;
                width: 30%%;
                text-align: center;
            }
            .foto img {
                width: 200px;
                heigth: 300px;
                border-radius: 10px;
                border: solid #fff 2px;
            }
            .datos {
                text-align:center;
                float: right;
                background-color: rgb(255,255,255);
                width: 60%;
                heigth: 90%;
                padding: 5px;
            }
            .dato {
                display: block;
                margin: 15px 0;
                color: #333;
                font-weight: bold;
            }
            #btn {
                display: block;
                margin: 20px auto;
            }
            a{
            text-decoration: none;
            }

        </style>
    </head>
    <body>
        <h1>Listado de Carnets</h1>
        <div>
    '''

    # Generar los carnets dinámicamente
    contador = 0
    for socio in socios:
        contador += 1
        carnet = f'''
        <div class="carnet" id="id{contador}">
            <div class="foto">
                <img src="{socio["foto"]}" alt="imagen_{socio["numero_carnet"]}">
            </div>
            <div class="datos">
                <span class="dato">{socio["nombre_apellidos"]}</span>
                <br>
                <span class="dato">{socio["fecha_nacimiento"]}</span>
                <br>
                <span class="dato">{socio["numero_carnet"]}</span>
            </div>
        </div>
        '''
        respuesta += carnet

    respuesta += '''</div>
            <a href="http://127.0.0.1:8000/app4_biblioteca/base/">
                <button id="btn">Ir a la página base</button>
            </a>
        </body></html>'''
    

    return HttpResponse(respuesta)