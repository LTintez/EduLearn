from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def alumnos(request):
    return render(request, 'alumno.html')
