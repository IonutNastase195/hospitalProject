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


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        exclude = ['user', 'active']
        fields = '__all__'
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address', 'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Enter your mobile number', 'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'profile_pic': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
