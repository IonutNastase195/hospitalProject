from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# DEPARTMENTS = [
#     ('cardiologist', 'Cardiologist'),
#     ('dermatologists', 'Dermatologists'),
#     ('emergency specialists', 'Emergency Specialists'),
#     ('allergists', 'Allergists'),
#     ('anesthesiologists', 'Anesthesiologists')
# ]