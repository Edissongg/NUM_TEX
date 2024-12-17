# convertir/urls.py
from django.urls import path
from .views import ConvertirNumero

urlpatterns = [
    path('projects/', ConvertirNumero.as_view(), name='projects'),
]
