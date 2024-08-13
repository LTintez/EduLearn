from django.shortcuts import redirect, render
from django.http import HttpResponse
<<<<<<< HEAD
from .models import Alumno
from .forms import AlumnoForm

=======
from django.contrib.auth.decorators import login_required
>>>>>>> 28bc65d23ee0505f0f85f07ed3fc89e716f450be
TEMPLATE_DIRS = {
    'os.path.join(BASE_DIR, "templates)'
}

@login_required
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