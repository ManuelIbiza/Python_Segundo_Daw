from django.urls import path
from . import views

app_name = "app3_json"

urlpatterns = [
    path("base/", views.base, name="base"),
    path("escritura_json/", views.escritura_json, name="escritura_json"),
    path("lectura_json/", views.lectura_json, name="lectura_json"),
    path("respuesta_json/", views.respuesta_json, name="respuesta_json"),
]