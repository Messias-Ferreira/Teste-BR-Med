"""
Modulo de URL do app
"""
from django.urls import path

from . import views


app_name = "conversor"

urlpatterns = [
    path("", views.index, name="index"),
    path("consulta", views.CotacoesList.as_view(), name="consulta")
]
