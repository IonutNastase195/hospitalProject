from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User, AbstractUser

from department.models import Department


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='static/doctors/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user.username
