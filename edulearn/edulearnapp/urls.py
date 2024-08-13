from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls.conf import include

urlpatterns = [
    path('', views.index, name='index'),
    path('alumno', views.alumnos, name='alumnos'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]