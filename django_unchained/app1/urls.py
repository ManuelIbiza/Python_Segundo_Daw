from django.urls import path
from . import views

app_name = "app1"

urlpatterns = [
    path("base/", views.base, name="base"),
]