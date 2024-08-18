from django.urls import path
from .views import AlumnoCreateView, AlumnoListView, AlumnoDeleteView, AlumnoUpdateView, ConsultaAlumnoView, InscribirAlumnoView, AlumnosInscriptosView

urlpatterns = [
    path('crear/', AlumnoCreateView.as_view(), name='alumno-create'),
    path('lista/', AlumnoListView.as_view(), name='alumno-list'),
    path('eliminar/<int:pk>/', AlumnoDeleteView.as_view(), name='alumno-delete'),
    path('editar/<int:pk>/', AlumnoUpdateView.as_view(), name='alumno-edit'),
    path('consultar/', ConsultaAlumnoView, name='alumno-consulta'),
    path('inscribir/', InscribirAlumnoView, name='alumno-inscribir'),
    path('alumnos-inscritos/', AlumnosInscriptosView, name='alumnos-inscritos-list'),

]