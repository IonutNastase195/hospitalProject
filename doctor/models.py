from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User, AbstractUser

from department.models import Department


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    profile_pic = models.ImageField(upload_to='static/doctors/', null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class DoctorSchedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    datetime_from = models.DateTimeField()
    datetime_to = models.DateTimeField()

    def __str__(self):
        return f"{self.doctor}, {self.datetime_from}, {self.datetime_to}"
