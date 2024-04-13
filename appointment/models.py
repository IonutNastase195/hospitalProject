from django.db import models
from django.utils import timezone
from datetime import timedelta
from doctor.models import Doctor
from patient.models import Patient


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    symptoms = models.CharField(max_length=100, null=False)
    appointment_date = models.DateTimeField(default=timezone.now)
    duration = models.DurationField(default=timedelta(minutes=30))
    description = models.TextField(max_length=500)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Appointment for {self.patient} with {self.doctor} on {self.appointment_date}"
