from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from department.forms import DepartmentCreateForm, DepartmentUpdateForm
from department.models import Department


class DepartmentCreateView(CreateView):
    template_name = 'department/create_department.html'
    model = Department
    form_class = DepartmentCreateForm
    success_url = reverse_lazy('list_department')


class DepartmentListView(ListView):
    template_name = 'department/list_department.html'
    context_object_name = 'all_departments'

    def get_queryset(self):
        return Department.objects.all()

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        departments = Department.objects.all()
        data['departments'] = departments
        return data


class DepartmentUpdateView(UpdateView):
    template_name = 'department/update_department.html'
    model = Department
    form_class = DepartmentUpdateForm
    success_url = reverse_lazy('list_department')


class DepartmentDeleteView(DeleteView):
    template_name = 'department/delete_department.html'
    model = Department
    success_url = reverse_lazy('list_department')


class DepartmentDetailView(DetailView):
    template_name = 'department/details_department.html'
    model = Department
