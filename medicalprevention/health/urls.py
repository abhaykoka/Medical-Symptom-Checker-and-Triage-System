# health/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.diagnose, name='diagnose'),
]
