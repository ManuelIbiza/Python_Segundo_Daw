from django.urls import path
from . import views

app_name = "app2"

urlpatterns = [
    path("base/", views.base, name="base"),
    path("resultado/", views.resultado, name="resultado")
]