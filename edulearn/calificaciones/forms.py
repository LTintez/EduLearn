from django import forms
from .models import Calificacion
from alumnos.models import Alumno
from cursos.models import Curso

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['alumno', 'curso', 'nota', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['alumno'].queryset = Alumno.objects.all()
        self.fields['curso'].queryset = Curso.objects.all()
