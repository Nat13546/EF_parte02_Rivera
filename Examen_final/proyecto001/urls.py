"""
URL configuration for proyecto001 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from miapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name = "inicio"),
    path('paises/', views.paises, name = "paises"),
    path('registrar_pais/',views.registrar_pais,name="registrar_pais"),
    path('eliminar_pais/<int:id_pais>/', views.eliminar_pais, name='eliminar_pais'),
    path('editoriales/',views.editoriales, name = "editoriales"),
    path('crear_editorial/',views.crear_editorial, name = "crear_editorial"),
]