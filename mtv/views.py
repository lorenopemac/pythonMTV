from django.shortcuts import render
from mtv.models import Familiar

# Create your views here.


def monstrarFamiliares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "mtv/familiares.html", {"lista_familiares": lista_familiares})

def saludarPersona(request, nombre, apellido):
    return render(request, "mtv/saludar.html", {"nombre": nombre, "apellido": apellido})
 

