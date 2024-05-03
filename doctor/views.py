import datetime
import zoneinfo
from _pydatetime import timedelta

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseServerError
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView

from appointment.models import Appointment
from doctor.filters import DoctorFilter
from doctor.forms import DoctorCreateForm, DoctorForm
from doctor.models import Doctor, DoctorSchedule
from hospital import settings
from patient.forms import CustomUserCreationForm, CustomUserUpdateForm


class DoctorListView(LoginRequiredMixin, ListView):
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


class DoctorDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'doctor/delete_doctor.html'
    model = Doctor
    success_url = reverse_lazy('list-doctor')


class DoctorDetailView(LoginRequiredMixin, DetailView):
    template_name = 'doctor/details_doctor.html'
    model = Doctor


class DoctorCreateView(LoginRequiredMixin, CreateView):
    template_name = 'doctor/create_doctor.html'
    form_class = DoctorCreateForm
    model = Doctor
    success_url = reverse_lazy('list-doctor')


class DoctorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'doctor/update_doctor.html'
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy('list-doctor')


def doctor_register_view(request):
    doctor_form = DoctorCreateForm()
    user_form = CustomUserCreationForm()
    if request.method == 'POST':
        doctor_form = DoctorCreateForm(request.POST)
        user_form = CustomUserCreationForm(request.POST)
        if doctor_form.is_valid() and user_form.is_valid():
            doctor = doctor_form.save(commit=False)
            user = user_form.save()
            doctor.user = user
            doctor.save()
            return redirect('list-doctor')
    return render(request, 'doctor/create_doctor.html', {'doctor_form': doctor_form, 'user_form': user_form})


@login_required
def update_doctor_view(request, pk):
    doctor = Doctor.objects.get(pk=pk)
    user = doctor.user

    if request.method == 'POST':
        doctor_form = DoctorForm(request.POST, instance=doctor)
        user_update_form = CustomUserUpdateForm(request.POST, instance=user)

        if doctor_form.is_valid() and user_update_form.is_valid():
            doctor_form.save()
            user_update_form.save()
            return redirect('list-doctor')
    else:
        doctor_form = DoctorForm(instance=doctor)
        user_update_form = CustomUserUpdateForm(instance=user)

    return render(request, 'doctor/update_doctor.html', {
        'doctor_update_form': doctor_form,
        'user_update_form': user_update_form
    })


@login_required
def doctor_schedule(doctor):
    PX_PER_HOUR = 50

    today = timezone.now()
    start_of_week = today - datetime.timedelta(days=today.weekday())
    end_of_week = start_of_week + datetime.timedelta(days=7)

    appointments = Appointment.objects.filter(datetime_from__gte=start_of_week, datetime_to__lte=end_of_week,
                                              doctor=doctor).order_by('datetime_from')
    doctor_schedules = DoctorSchedule.objects.filter(datetime_from__gte=start_of_week, datetime_to__lte=end_of_week,
                                                     doctor=doctor)
    calendar_data = {}

    header_col = []
    start_hour = 9
    end_hour = 20
    for index, i in enumerate(range(start_hour, end_hour + 1)):
        header_col.append({
            'value': f'{i}:00',
            'top': (PX_PER_HOUR if index != 0 else 0),
            'height': PX_PER_HOUR - 34
        })
    for day in range(7):
        current_day = start_of_week + datetime.timedelta(days=day)
        calendar_data[current_day] = {'appointments': [], 'doctor_schedules': []}
        appointments_for_day = appointments.filter(datetime_from__date=current_day, datetime_to__date=current_day)
        doctor_schedules_for_day = doctor_schedules.filter(datetime_from__date=current_day,
                                                           datetime_to__date=current_day)
        last_bottom = 0
        for a in appointments_for_day:
            a.height = int((a.datetime_to - a.datetime_from).total_seconds() / 3600 * PX_PER_HOUR)
            a.top = int(abs(a.datetime_from - timezone.datetime(a.datetime_from.year, a.datetime_from.month,
                                                                a.datetime_from.day, hour=start_hour,
                                                                tzinfo=zoneinfo.ZoneInfo(
                                                                    settings.TIME_ZONE))).total_seconds() / 3600 * PX_PER_HOUR) - last_bottom
            last_bottom += a.height + a.top
            a.top += 17
        calendar_data[current_day]['appointments'] = appointments_for_day
        calendar_data[current_day]['doctor_schedules'] = doctor_schedules_for_day
    calendar_data['header'] = header_col
    return calendar_data


@login_required
def doctor_schedule_view(request):
    if request.user.is_authenticated:
        doctor = Doctor.objects.filter(user=request.user).first()
        if doctor:
            calendar_data = doctor_schedule(doctor)

            return render(request, 'doctor/doctor_schedule.html', {'calendar_data': calendar_data, 'doctor': doctor})
        else:
            return HttpResponseServerError("You are not registered as a doctor.")
    else:
        return HttpResponseServerError("You are not logged in.")


def get_intersecting_appointments(doctor):
    appointments = Appointment.objects.filter(doctor=doctor)

    intersecting_count = 0

    for i, appointment1 in enumerate(appointments):
        for appointment2 in appointments[i + 1:]:
            if (appointment1.datetime_from < appointment2.datetime_to and
                    appointment1.datetime_to > appointment2.datetime_from):
                intersecting_count += 1

    return intersecting_count
