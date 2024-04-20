from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput

from patient.models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ['user', 'active', 'address', 'profile_pic']
        fields = '__all__'
        widgets = {
            'address': TextInput(attrs={'placeholder': 'Enter your address', 'class': 'form-control'}),
            'mobile': TextInput(attrs={'placeholder': 'Enter your mobile number', 'class': 'form-control'}),
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter your first name', 'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter your last name', 'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter your username', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email', 'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter your password', 'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm your password', 'class': 'form-control'})


class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
