# Generated by Django 5.0.4 on 2024-04-20 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_patient_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='active',
        ),
    ]
