from django.urls import path
from .views import CursoCreateView, CursoListView, CursoDeleteView

urlpatterns = [
    path('crear/', CursoCreateView.as_view(), name='curso-create'),
    path('lista/', CursoListView.as_view(), name='curso-list'),
    path('eliminar/<int:pk>/', CursoDeleteView.as_view(), name='curso-delete'),
]