from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {"message": "Cam greu sa programezi :("}
    return render(request, "universities/index.html", context)