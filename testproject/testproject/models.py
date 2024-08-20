from django.db import models

class Patient(models.Model):
    patient_name = models.CharField(max_length=255)
    blood_group = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.patient_name} - {self.blood_group}"