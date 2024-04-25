from django import forms
from django.forms import TextInput

from appointment.models import Appointment


class AppointmentCreateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
