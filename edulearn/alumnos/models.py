from django.db import models

from django.db import models
from cursos.models import Curso

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()

    cursos = models.ManyToManyField(Curso, related_name='alumnos', through='Inscripcion')  # Relación muchos a muchos

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('alumno', 'curso')  # Asegura que un alumno no se inscriba en el mismo curso más de una vez

