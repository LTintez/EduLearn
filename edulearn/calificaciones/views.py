from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Calificacion, Alumno
from .forms import CalificacionForm

class CrearCalificacionView(CreateView):
    model = Calificacion
    form_class = CalificacionForm
    template_name = 'calificacionform.html'
    success_url = reverse_lazy('calificaciones-listar') 

    def form_valid(self, form):
        return super().form_valid(form)

class ListarCalificacionView(ListView):
    model = Calificacion
    template_name = 'calificacioneslist.html'
    context_object_name = 'calificaciones'
    
    def get_queryset(self):
        return Calificacion.objects.all()

class BuscarCalificacionesView(ListView):
    template_name = 'calificacionesbuscar.html'
    context_object_name = 'calificaciones'
    
    def get_queryset(self):
        dni = self.request.GET.get('dni')
        if dni:
            alumno = get_object_or_404(Alumno, dni=dni)
            return Calificacion.objects.filter(alumno=alumno)
        return Calificacion.objects.none()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dni = self.request.GET.get('dni')
        if dni:
            context['alumno'] = get_object_or_404(Alumno, dni=dni)
        return context
