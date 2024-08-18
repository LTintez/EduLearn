from django.urls import path
from .views import CrearCalificacionView, ListarCalificacionView, BuscarCalificacionesView

urlpatterns = [
    path('nueva-calificacion/', CrearCalificacionView.as_view(), name='nueva-calificacion'),
    path('listar/', ListarCalificacionView.as_view(), name='calificaciones-listar'),
    path('buscar-calificaciones/', BuscarCalificacionesView.as_view(), name='buscar-calificaciones'),
]
