"""proyectoGit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import hola
from .views import fecha
from .views import calcular_fecha_nacimiento
from .views import mi_template
from .views import tu_template
from .views import prueba_template
from .views import ver_personas
from .views import crear_persona


urlpatterns = [
    path('hola/', hola),
    path('fecha/', fecha),
    path('fecha-nacimiento/<int:edad>', calcular_fecha_nacimiento),
    path('mi-template/', mi_template),
    path('mi-template/<str:nombre>', tu_template),
    path('prueba-template/', prueba_template),
    path('ver-personas/', ver_personas),
    path('crear-persona/<str:nombre>/<str:apellido>/', crear_persona),
    path('admin/', admin.site.urls),
]
