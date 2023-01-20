"""clinicmaster URL Configuration

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
from django.urls import path, include
from .views import (allergies_Page,patients_Page,visits_Page,patientsGeneralPage)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('common/', include('common.urls')),
    path('', allergies_Page),
    path('patients/', patients_Page),
    path('visits/', visits_Page),
    path('patientsGeneral',patientsGeneralPage),
    path('admin/', admin.site.urls),
]

urlpatterns+=staticfiles_urlpatterns()

admin.site.site_header = "ClinicMaster"
admin.site.site_title = "ClinicMaster"
admin.site.index_title = "Welcome to ClinicMaster"