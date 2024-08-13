from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Alumno
from .forms import AlumnoForm

TEMPLATE_DIRS = {
    'os.path.join(BASE_DIR, "templates)'
}

def index(request):
    return render(request, 'index.html')

def alumnos(request):
    return render(request, 'alumno.html')

def registrar_alumno(request):
    #if request.method == 'POST':
    #    form = AlumnoForm(request.POST)
    #    if form.is_valid():
    #        form.save()
    #        return redirect('lista_alumnos')
    #else:
    #    form = AlumnoForm()
    return render(request, 'registrar_alumno.html')


def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos/lista_alumnos.html', {'alumnos': alumnos})