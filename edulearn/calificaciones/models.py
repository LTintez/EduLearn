from django.db import models
from alumnos.models import Alumno
from cursos.models import Curso

class Calificacion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 11)])
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.alumno.nombre} - {self.curso.nombre} - Nota: {self.nota}"