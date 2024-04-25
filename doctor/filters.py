import django_filters
from django import forms

from department.models import Department
from doctor.models import Doctor


class DoctorFilter(django_filters.FilterSet):
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
    department = django_filters.ModelChoiceFilter(queryset=Department.objects.order_by('name').distinct(),
                                                  label='Department', empty_label='All Departments',
                                                  widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'email', 'department', 'address', 'mobile']
