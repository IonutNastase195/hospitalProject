from django.urls import path
from appointment import views

urlpatterns = [
    path('create_appointment', views.AppointmentCreateView.as_view(), name='create-appointment'),
    path('list_appointment', views.AppointmentListView.as_view(), name='list-appointment'),
    path('update_appointment/<int:pk>', views.AppointmentUpdateView.as_view(), name='update-appointment'),
    path('delete_appointment/<int:pk>', views.AppointmentDeleteView.as_view(), name='delete-appointment'),
    path('detail_appointment/<int:pk>', views.AppointmentDetailView.as_view(), name='detail-appointment')
]
