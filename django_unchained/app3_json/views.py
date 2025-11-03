from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import pprint
import json
import os # Para generar rutas

def base(request):
    return render(request, 'app3_json/base.html')

def escritura_json(request):
    # Datos que queremos guardar en JSON
    datos = {
        "usuarios": [
            {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
            {"nombre": "María", "edad": 30, "ciudad": "Barcelona"},
            {"nombre": "Pedro", "edad": 22, "ciudad": "Valencia"},
            {"nombre": "Luisa", "edad": 22, "ciudad": "Mallorca"}
        ],
        "total_usuarios": 4,
        "fecha_creacion": "2025-01-01"
    }

    # Ruta donde guardaremos el archivo
    ruta_archivo = os.path.join(settings.BASE_DIR, "app3_json\data\datos_escritura.json")

    try:
        print("\nVoy a escribir los siguientes datos:\n")
        # Damos formato para presentar los datos
        pprint.pprint(datos)

        # Escribimos en el archivo JSON
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            # La función dump nos permite SERIALIZAR un objeto. Es decir, pasar un objeto a un formato para almacenar
            # o transmitir y que en este caso sería JSON
            # Indicamos que la indentación sea por tabulación
            json.dump(datos, archivo, indent="\t")

        return HttpResponse("<h1>Escribiendo datos en JSON... ok</h1>")

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def respuesta_json(request):
    return render(request, "app3_json/respuesta_json.html")

def lectura_json(request):
    # Hemos importado el fichero settings.py para obtener la ruta base y le añadimos lo que falte hasta el JSON
    ruta_json = os.path.join(settings.BASE_DIR, "app3_json/data", "datos_lectura.json")

    # Leemos el fichero JSON y lo almacenamos en la variable datos.
    # Esto lo denominamos DESERIALIZAR. Es decir pasamos de un formato de estructura/almacenaje
    # como JSON a un objeto.
    try:
        with open(ruta_json, "r", encoding="utf-8") as file:
            datos = json.load(file)
    except Exception as e:
        datos = {"error": str(e)}

    # Pasamos los datos directamente al template
    return render(request, "app3_json/respuesta_json.html", {'datos': datos})