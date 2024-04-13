from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from patient.forms import PatientForm
from patient.models import Patient


class PatientCreateView(CreateView):
    template_name = 'patient/create_patient.html'
    model = Patient
    form_class = PatientForm
    success_url = reverse_lazy('home_page')
