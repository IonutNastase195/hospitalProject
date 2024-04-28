from django.urls import path
from doctor import views

urlpatterns = [
    path('create_doctor', views.doctor_register_view, name='create-doctor'),
    path('list_doctor', views.DoctorListView.as_view(), name='list-doctor'),
    path('update_doctor/<int:pk>', views.update_doctor_view, name='update-doctor'),
    path('delete_doctor/<int:pk>', views.DoctorDeleteView.as_view(), name='delete-doctor'),
    path('detail_doctor/<int:pk>', views.DoctorDetailView.as_view(), name='detail-doctor'),
    path('doctor_schedule', views.doctor_schedule_view, name='doctor-schedule'),
]
