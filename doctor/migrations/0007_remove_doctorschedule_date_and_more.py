# Generated by Django 5.0.4 on 2024-04-27 08:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_doctorschedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorschedule',
            name='date',
        ),
        migrations.RemoveField(
            model_name='doctorschedule',
            name='time_from',
        ),
        migrations.RemoveField(
            model_name='doctorschedule',
            name='time_to',
        ),
        migrations.AddField(
            model_name='doctorschedule',
            name='datetime_from',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctorschedule',
            name='datetime_to',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]