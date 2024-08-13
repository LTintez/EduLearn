from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls.conf import include

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('alumnos/', views.registrar_alumno, name='registrar_alumno'),
    path('registrar/', views.lista_alumnos, name='lista_alumnos'),
=======
    path('alumno', views.alumnos, name='alumnos'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
>>>>>>> 28bc65d23ee0505f0f85f07ed3fc89e716f450be
]