from rest_framework import serializers
from .models import PatientDoctorMapping

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = '__all__'
