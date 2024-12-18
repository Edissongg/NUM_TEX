"""
URL configuration for API_NAT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include

def api_home(request):
    return HttpResponse("Bienvenido a la API_NAT. Use '/api/' para los endpoints disponibles.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_home, name='api_home'),  # Vista para el endpoint raíz
    path('api/', include('projects.urls')),  # Incluye las rutas de la app projects
]
