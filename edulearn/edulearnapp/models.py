from django.db import models

class Curso(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Alumno(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.ForeignKey(Curso, on_delete=models.CASCADE)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2)

    def calculate_average(self):
        return self.calificacion

    def get_status(self):
        if self.calificacion >= 90:
            return 'Excelente'
        elif 70 <= self.calificacion < 90:
            return 'Bueno'
        else:
            return 'En riesgo'

    def __str__(self):
        return self.name