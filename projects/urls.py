from django.urls import path
from .views import ConvertirNumero

app_name = 'projects'

urlpatterns = [
    path('projects/', ConvertirNumero.as_view(), name='projects'),
]
