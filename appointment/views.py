from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView

from appointment.forms import AppointmentCreateForm, AppointmentUpdateForm
from appointment.models import Appointment


class AppointmentCreateView(CreateView):
    template_name = 'appointment/create_appointment.html'
    model = Appointment
    form_class = AppointmentCreateForm
    success_url = reverse_lazy('list-appointment')


class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointment/list_appointments.html'
    context_object_name = 'all_appointments'


class AppointmentUpdateView(UpdateView):
    template_name = 'appointment/update_appointment.html'
    model = Appointment
    form_class = AppointmentUpdateForm
    success_url = reverse_lazy('list-appointment')


class AppointmentDeleteView(DeleteView):
    template_name = 'appointment/delete_appointment.html'
    model = Appointment
    success_url = reverse_lazy('list-appointment')


class AppointmentDetailView(DetailView):
    template_name = 'appointment/details_appointment.html'
    model = Appointment
