from django import forms
from django.forms import TextInput, EmailInput

from patient.models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'address': TextInput(attrs={'placeholder': 'Enter your address', 'class': 'form-control'}),
            'mobile': TextInput(attrs={'placeholder': 'Enter your mobile number', 'class': 'form-control'}),
            'user__username': TextInput(attrs={'placeholder': 'Enter your username', 'class': 'form-control'}),
            'user__email': EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control'}),
        }


class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
