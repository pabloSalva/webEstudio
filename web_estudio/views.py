from django.shortcuts import render

from .models import Turno

def index(request):
    return render(request, 'turnos/index.html')
    

def turnos(request):
    return render(request, 'turnos/turnos.html')


def civil_comercial(request):
    return render(request, 'turnos/civilcomercial.html')

def laboral(request):
    return render(request, 'turnos/laboral.html')    
