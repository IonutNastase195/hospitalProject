from django.urls import path
from patient import views

urlpatterns = [
    path('create_patient', views.patient_register_view, name='create-patient'),
    path('list_patients', views.PatientListView.as_view(), name='list-patient'),
    path('update_patient/<int:pk>/', views.update_patient_view, name='update-patient'),
    path('delete_patient/<int:pk>/', views.PatientDeleteView.as_view(), name='delete-patient'),
    path('detail_patient/<int:pk>/', views.PatientDetailView.as_view(), name='detail-patient'),
    path('history_patient/', views.HistoryPatientListView.as_view(), name='history-patient')
]
