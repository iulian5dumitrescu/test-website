from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("catalogfacultati/", views.catalog_facultati, name = "catalogfacultati")
]
