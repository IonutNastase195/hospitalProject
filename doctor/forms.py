from django import forms
from django.forms import TextInput, Select

from doctor.models import Doctor


class DoctorCreateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        exclude = ['user', 'address', 'active', 'profile_pic']
        fields = '__all__'
        widgets = {
            'department': Select(attrs={'class': 'form-control', 'placeholder': 'Choose the department'}),
            'address': TextInput(attrs={'placeholder': 'Enter your address', 'class': 'form-control'}),
            'mobile': TextInput(attrs={'placeholder': 'Enter your mobile number', 'class': 'form-control'}),
        }


class DoctorUpdateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

    widgets = {
        'address': TextInput(attrs={'placeholder': 'Enter your address', 'class': 'form-control'}),
        'mobile': TextInput(attrs={'placeholder': 'Enter your mobile number', 'class': 'form-control'}),
    }
