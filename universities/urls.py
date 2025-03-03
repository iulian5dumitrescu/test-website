from django.urls import path
from . import views

urlpatterns = [
    path("", views.ecran_principal, name="ecran_principal"),
    path("facultatiromania/", views.facultati_romania, name = "facultatiromania"),
    path("catalogfacultati/", views.catalog_facultati, name = "catalogfacultati"),
    path("bibliografie/", views.bibliografie, name = "bibliografie"),
]
