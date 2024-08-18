from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import Dashboard


urlpatterns = [
    path('dashboard/',login_required(Dashboard.as_view()),name='dashboard' )
]