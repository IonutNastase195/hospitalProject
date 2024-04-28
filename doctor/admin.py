from django.contrib import admin

from doctor.models import Doctor, DoctorSchedule

admin.site.register(Doctor)
admin.site.register(DoctorSchedule)
