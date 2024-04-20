from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView

from doctor.filters import DoctorFilter
from doctor.forms import DoctorForm, DoctorUpdateForm
from doctor.models import Doctor
from patient.forms import CustomUserCreationForm


class DoctorCreateView(CreateView):
    template_name = 'doctor/create_doctor.html'
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy('home_page')


class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctor/list_doctors.html'
    context_object_name = 'all_doctors'

    def get_queryset(self):
        return Doctor.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        doctors = Doctor.objects.filter(active=True)
        myFilter = DoctorFilter(self.request.GET, queryset=doctors)
        doctors = myFilter.qs
        data['all_doctors'] = doctors
        data['filters'] = myFilter.form

        return data


class DoctorUpdateView(UpdateView):
    template_name = 'doctor/update_doctor.html'
    model = Doctor
    form_class = DoctorUpdateForm
    success_url = reverse_lazy('list-doctor')


class DoctorDeleteView(DeleteView):
    template_name = 'doctor/delete_doctor.html'
    model = Doctor
    success_url = reverse_lazy('list-doctor')


class DoctorDetailView(DetailView):
    template_name = 'doctor/details_doctor.html'
    model = Doctor


def doctor_register_view(request):
    doctor_form = DoctorForm()
    user_form = CustomUserCreationForm()
    if request.method == 'POST':
        doctor_form = DoctorForm(request.POST)
        user_form = CustomUserCreationForm(request.POST)
        if doctor_form.is_valid() and user_form.is_valid():
            doctor = doctor_form.save(commit=False)
            user = user_form.save()
            doctor.user = user
            doctor.save()
            return redirect('list-doctor')
    return render(request, 'doctor/create_doctor.html', {'doctor_form': doctor_form, 'user_form': user_form})
