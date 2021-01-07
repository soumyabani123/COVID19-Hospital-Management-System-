"""covid_hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
import os
from covidproject import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django_filters.views import FilterView

from covidproject.filters import patientfilter


urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.login),
    path('home/', views.home, name='home'),
    path('patient_details',views.patient_details,name='patient_details'),
    path('doctor_details',views.doctor_details,name='doctor_details'),
    path('ward_details',views.ward_details,name='ward_details'),
    path('staff_details',views.staff_details,name='staff_details'),
    path('admit_info_details',views.admit_info_details,name='admit_info_details'),
    path('discharge_info_details',views.discharge_info_details,name='discharge_info_details'),
    path('addpatient',views.addpatient,name='addpatient'),
    path('patient_details',FilterView.as_view(filterset_class=patientfilter,
        template_name='search/patientfilter.html'),name='search'),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

