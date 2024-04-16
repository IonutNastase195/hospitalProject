import django_filters
from django import forms

from patient.models import Patient


class PatientFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(field_name='user__first_name', lookup_expr='icontains', label='First name',
                                           widget=forms.TextInput(
                                               attrs={'class': 'form-control',
                                                      'placeholder': 'Please enter first name'}))

    last_name = django_filters.CharFilter(field_name='user__last_name', lookup_expr='icontains', label='Last name',
                                          widget=forms.TextInput(
                                              attrs={'class': 'form-control',
                                                     'placeholder': 'Please enter last name'}))
    email = django_filters.CharFilter(field_name='user__email', lookup_expr='icontains', label='Email',
                                      widget=forms.TextInput(
                                          attrs={'class': 'form-control',
                                                 'placeholder': 'Please enter email'}))
    address = django_filters.CharFilter(lookup_expr='icontains', label='Address',
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control',
                                                   'placeholder': 'Please enter address'}))
    mobile = django_filters.CharFilter(lookup_expr='icontains', label='Mobile',
                                       widget=forms.TextInput(
                                           attrs={'class': 'form-control',
                                                  'placeholder': 'Please enter mobile'}))

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'email', 'address', 'mobile']
