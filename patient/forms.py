from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, ClearableFileInput

from patient.models import Patient

from django import forms


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ['user', 'active']
        fields = '__all__'
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address', 'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Enter your mobile number', 'class': 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'})
        }

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not mobile.isdigit() or len(mobile) != 10:
            raise forms.ValidationError("Invalid mobile number format")
        return mobile


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


class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        exclude = ['password']
        fields = ['first_name', 'last_name', 'email', 'username']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter your first name', 'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter your last name', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email', 'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter your username', 'class': 'form-control'})
