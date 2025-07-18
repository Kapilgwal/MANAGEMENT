from django.db import models
import uuid

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    specialty = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
