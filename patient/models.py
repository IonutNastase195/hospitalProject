from django.contrib.auth.models import User
from django.db import models


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    active = models.BooleanField(default=True)
    profile_pic = models.ImageField(upload_to='media/patients/', null=True, blank=True)

    def __str__(self):
        return self.user.username

