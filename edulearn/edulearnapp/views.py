from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
TEMPLATE_DIRS = {
    'os.path.join(BASE_DIR, "templates)'
}

@login_required
def index(request):
    return render(request, 'index.html')


def alumnos(request):
    return render(request, 'alumno.html')
