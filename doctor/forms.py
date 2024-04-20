from django import forms
from django.forms import TextInput

from doctor.models import Doctor


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        exclude = ['user', 'address', 'active', 'profile_pic']
        fields = '__all__'
        widgets = {
            'department': TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose the department'}),
            'address': TextInput(attrs={'placeholder': 'Enter your address', 'class': 'form-control'}),
            'mobile': TextInput(attrs={'placeholder': 'Enter your mobile number', 'class': 'form-control'}),
        }


class DoctorUpdateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
