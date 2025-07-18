from django.db import models
import uuid

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    disease = models.CharField(max_length=100)
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name
