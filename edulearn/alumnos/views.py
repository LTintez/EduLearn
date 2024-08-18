from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .forms import AlumnoForm, InscripcionForm
from .models import Alumno, Inscripcion
from .forms import DNIConsultaForm

class AlumnoCreateView(View):
    def get(self, request):
        form = AlumnoForm()
        return render(request, 'alumnoscreate.html', {'form': form})

    def post(self, request):
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumno-list')
        return render(request, 'alumnoscreate.html', {'form': form})
    
class AlumnoListView(ListView):
    model = Alumno
    template_name = 'alumnoslist.html'
    context_object_name = 'alumnos'

    def get_queryset(self):
        return Alumno.objects.all()
    
class AlumnoDeleteView(View):
    def post(self, request, pk):
        alumno = get_object_or_404(Alumno, pk=pk)
        alumno.delete()
        return redirect('alumno-list')
    
class AlumnoUpdateView(UpdateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'alumnosedit.html'
    success_url = reverse_lazy('alumno-list')

def ConsultaAlumnoView(request):
    form = DNIConsultaForm()
    alumno = None

    if request.method == 'POST':
        form = DNIConsultaForm(request.POST)
        if form.is_valid():
            dni = form.cleaned_data['dni']
            alumno = get_object_or_404(Alumno, dni=dni)

    return render(request, 'alumnoconsulta.html', {'form': form, 'alumno': alumno})

def InscribirAlumnoView(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            alumno = form.cleaned_data['alumno']
            curso = form.cleaned_data['curso']
            curso.alumnos.add(alumno)
            curso.save()
            return redirect('alumnos-inscritos-list')
    else:
        form = InscripcionForm()

    return render(request, 'alumnoinscp.html', {'form': form})

def AlumnosInscriptosView(request):
    inscripciones = Inscripcion.objects.select_related('alumno', 'curso').all()
    return render(request, 'alumnoinscplist.html', {'inscripciones': inscripciones})