from django.urls import path
from . import views

app_name = "app4_biblioteca"

urlpatterns = [
    path("base/", views.base, name="base"),
    path("mostrar_todos/", views.mostrar_todos, name="mostrar_todos"),
    path("mostrar_uno/", views.mostrar_uno, name="mostrar_uno"),
]