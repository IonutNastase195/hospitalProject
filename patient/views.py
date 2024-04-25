from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models.functions import datetime
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from patient.filters import PatientFilter
from patient.forms import PatientForm, CustomUserCreationForm, CustomUserUpdateForm
from patient.models import Patient, HistoryPatient


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


class PatientDeleteView(DeleteView):
    template_name = 'patient/delete_patient.html'
    model = Patient
    success_url = reverse_lazy('list-patient')


class PatientDetailView(DetailView):
    template_name = 'patient/details_patient.html'
    model = Patient


def patient_register_view(request):
    patient_form = PatientForm()
    user_form = CustomUserCreationForm()
    if request.method == 'POST':
        patient_form = PatientForm(request.POST)
        user_form = CustomUserCreationForm(request.POST)
        if patient_form.is_valid() and user_form.is_valid():
            user = user_form.save()
            patient = patient_form.save(commit=False)
            patient.user = user
            patient.save()
            history_patient = (f'The following patient was added: '
                               f'first_name:{patient.user.first_name}, '
                               f'last_name:{patient.user.last_name}, '
                               f'email: {patient.user.email}')

            HistoryPatient.objects.create(message=history_patient, created_at=datetime.datetime.now(), active=True,
                                          user=User.objects.get(id=patient.user.id))
            return redirect(reverse_lazy('login'))
    return render(request, 'patient/create_patient.html',
                  {'patient_form': patient_form, 'user_form': user_form})


class HistoryPatientListView(ListView):
    template_name = 'patient/history_patient.html'
    model = HistoryPatient
    context_object_name = 'all_patient_history'

    def get_queryset(self):
        return HistoryPatient.objects.filter()


def update_patient_view(request, pk):
    patient = Patient.objects.get(pk=pk)
    user = patient.user

    if request.method == 'POST':
        patient_form = PatientForm(request.POST, instance=patient)
        user_update_form = CustomUserUpdateForm(request.POST, instance=user)

        if patient_form.is_valid() and user_update_form.is_valid():
            patient_form.save()
            user_update_form.save()
            return redirect('list-patient')
    else:
        patient_form = PatientForm(instance=patient)
        user_update_form = CustomUserUpdateForm(instance=user)

    return render(request, 'patient/update_patient.html', {
        'patient_update_form': patient_form,
        'user_update_form': user_update_form
    })
