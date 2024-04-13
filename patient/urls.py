from django.urls import path

from patient import views
from patient.views import PatientCreateView

urlpatterns = [
    path('create_patient', views.PatientCreateView.as_view(), name='create-patient'),
]
