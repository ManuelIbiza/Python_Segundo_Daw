from django.http import HttpResponse
from django.shortcuts import render
from django.core.cache import cache
from datetime import datetime
import random

def base(request):
    return render(request, "app2/base.html")

def contador_s(request, cont):
    print("Entramos en contador_s")
    # Obtener o inicializar variable de sesión
    contador_session = request.session.get('contador', 0)

    # Guardar en sesión
    request.session['contador'] = contador_session + 1
    request.session['ultima_visita'] = str(datetime.now())

def generar_numero(request):
    print("Entramos en generar numero!")

    # Intentamos leer el número de la sesión SIN romper si no existe
    numero = request.session.get('numero')   # ← OJITO: .get('numero')

    if numero is None:                      # si no existe, lo creamos
        numero = random.randint(0, 1000)
        request.session['numero'] = numero  # y lo guardamos en la sesión

    return numero

def resultado(request):
    print("Entramos en resultado")
    contador_cache =cache.get('contador_global', 0)
    contador_cache +=1

    numero = generar_numero(request)

    cache.set('contador_global', contador_cache, 3600)

    contador_s(request, contador_cache)

    supuesto = int(request.GET.get("texto1", ""))
    print(numero)
    if supuesto < numero:
        return HttpResponse(f"""<h3 style="color: blue;">
            EL NÚMERO ES MAYOR QUE {supuesto} </h3>
        """)
    elif supuesto > numero:
        return HttpResponse(f"""
            <h3 style="color: red;">EL NÚMERO ES MENOR QUE {supuesto}</h3>
        """)
    else:
        numero = request.session.get('contador', 0)
        request.session['contador'] = 0
        request.session['numero'] = None
        return HttpResponse(f"""
            <h1 style="color: green;">Resultado</h1>
            <p>HAS ACERTADO! EL NÚMERO ES {supuesto}. </p>
            <p>Veces intentado:  </p>
            <p>{contador_cache} Según cache.</p>
            <p>{numero} Según sesión.</p>
        """)
