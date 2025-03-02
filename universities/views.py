from django.shortcuts import render
from django.http import HttpResponse
from .models import Facultate

# Create your views here.

def home(request):
    context = {"message": "Cam greu sa programezi :("}
    return render(request, "universities/meniu.html", context)

def catalog_facultati(request):
    items = Facultate.objects.all()
    return render(request, "universities/catalogfacultati.html", {"facultati": items} )