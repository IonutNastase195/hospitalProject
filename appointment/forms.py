from django import forms

from appointment.models import Appointment


class AppointmentCreateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'symptoms', 'description', 'datetime_from', 'datetime_to']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select patient'}),
            'doctor': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select doctor'}),
            'symptoms': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter symptoms'}),
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 50, 'class': 'form-control', 'placeholder': 'Enter description'}),
            'datetime_from': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'datetime_to': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }


class AppointmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'symptoms', 'description', 'datetime_from', 'datetime_to']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select patient'}),
            'doctor': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select doctor'}),
            'symptoms': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter symptoms'}),
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 50, 'class': 'form-control', 'placeholder': 'Enter description'}),
            'datetime_from': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'datetime_to': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }
