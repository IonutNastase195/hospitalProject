import zoneinfo

from django.test import TestCase
from django.utils import timezone

from appointment.models import Appointment
from doctor.models import Doctor
from doctor.views import get_intersecting_appointments
from hospital import settings


class DoctorTests(TestCase):
    def setUp(self):
        doctor = Doctor.objects.create(address='Test Doctor')
        Appointment.objects.create(
            doctor=doctor,
            datetime_from=timezone.datetime(2024, 5, 5, 13, 0, 0, tzinfo=zoneinfo.ZoneInfo(settings.TIME_ZONE)),
            datetime_to=timezone.datetime(2024, 5, 5, 15, 0, 0, tzinfo=zoneinfo.ZoneInfo(settings.TIME_ZONE)),
        )

    def test_appointment_unsuccessful(self):
        doctor = Doctor.objects.filter(address='Test Doctor').first()
        appointment = Appointment(
            doctor=doctor,
            datetime_from=timezone.datetime(2024, 5, 5, 12, 0, 0, tzinfo=zoneinfo.ZoneInfo(settings.TIME_ZONE)),
            datetime_to=timezone.datetime(2024, 5, 5, 14, 0, 0, tzinfo=zoneinfo.ZoneInfo(settings.TIME_ZONE))
        )
        appointments_intersecting = get_intersecting_appointments(doctor=doctor)
        self.assertEqual(appointments_intersecting, 1)

    def test_appointment_successful(self):
        doctor = Doctor.objects.filter(address='Test Doctor').first()
        appointment = Appointment(
            doctor=doctor,
            datetime_from=timezone.datetime(2024, 5, 5, 11, 0, 0, tzinfo=zoneinfo.ZoneInfo(settings.TIME_ZONE)),
            datetime_to=timezone.datetime(2024, 5, 5, 12, 0, 0, tzinfo=zoneinfo.ZoneInfo(settings.TIME_ZONE))
        )
        appointments_intersecting = get_intersecting_appointments(doctor=doctor)
        self.assertEqual(appointments_intersecting, 0)

    def tearDown(self):
        doctors = Doctor.objects.filter(address='Test Doctor')
        Appointment.objects.filter(doctor__in=doctors).delete()
        doctors.delete()
