from django import forms
from .models import Alumno, Curso

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'dni', 'email', 'telefono', 'fecha_nacimiento']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'email': forms.EmailInput(),
        }

class InscripcionForm(forms.Form):
    alumno = forms.ModelChoiceField(queryset=Alumno.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

class DNIConsultaForm(forms.Form):
    dni = forms.CharField(label='DNI', max_length=20, widget=forms.TextInput)
