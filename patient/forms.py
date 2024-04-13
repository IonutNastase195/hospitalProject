from django import forms
from django.forms import TextInput, EmailInput, Textarea, Select, NumberInput, DateInput

from patient.models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'