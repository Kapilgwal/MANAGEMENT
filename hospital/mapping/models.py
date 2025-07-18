import uuid
from django.db import models
from patient.models import Patient
from doctor.models import Doctor

class PatientDoctorMapping(models.Model):
    class Meta:
        unique_together = ('patient', 'doctor') 

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('pending', 'Pending')
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
