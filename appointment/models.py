from django.db import models
from django.utils import timezone
from doctor.models import Doctor
from patient.models import Patient


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    symptoms = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=500)
    datetime_from = models.DateTimeField(default=timezone.now)
    datetime_to = models.DateTimeField(default=timezone.now)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Appointment for {self.patient} with {self.doctor} "\
               f"on {self.datetime_from.strftime('%Y-%m-%d %H:%M')} "\
               f"to {self.datetime_to.strftime('%Y-%m-%d %H:%M')} "\
               f"| Symptoms: {self.symptoms} | Confirmed: {self.confirmed}"
