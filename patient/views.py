from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from patient.filters import PatientFilter
from patient.forms import PatientForm, PatientUpdateForm
from patient.models import Patient


class PatientCreateView(CreateView):
    template_name = 'patient/create_patient.html'
    model = Patient
    form_class = PatientForm
    success_url = reverse_lazy('home_page')


class PatientListView(ListView):
    model = Patient
    template_name = 'patient/list_patients.html'
    context_object_name = 'all_patients'

    def get_queryset(self):
        return Patient.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        patients = Patient.objects.filter(active=True)
        myFilter = PatientFilter(self.request.GET, queryset=patients)
        patients = myFilter.qs
        data['all_patients'] = patients
        data['filters'] = myFilter.form

        return data


class PatientUpdateView(UpdateView):
    template_name = 'patient/update_patient.html'
    model = Patient
    form_class = PatientUpdateForm
    success_url = reverse_lazy('list-patient')


class PatientDeleteView(DeleteView):
    template_name = 'patient/delete_patient.html'
    model = Patient
    success_url = reverse_lazy('list-patient')


class PatientDetailView(DetailView):
    template_name = 'patient/details_patient.html'
    model = Patient
