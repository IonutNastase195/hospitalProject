from django.urls import path
from department import views

urlpatterns = [
    path('create_department', views.DepartmentCreateView.as_view(), name='create-department'),
    path('list_department', views.DepartmentListView.as_view(), name='list-department'),
    path('update_department/<int:pk>', views.DepartmentUpdateView.as_view(), name='update-department'),
    path('delete_department/<int:pk>', views.DepartmentDeleteView.as_view(), name='delete-department'),
    path('detail_department/<int:pk>', views.DepartmentDetailView.as_view(), name='detail-department')
]
