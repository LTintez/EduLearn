from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls.conf import include

urlpatterns = [
    path('', views.index, name='index'),
    path('alumnos/', views.registrar_alumno, name='registrar_alumno'),
    path('registrar/', views.lista_alumnos, name='lista_alumnos'),
]