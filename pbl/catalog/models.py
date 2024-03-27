
from django.db import models
from django.urls import reverse

class doctor_model(models.Model):
    doctor_name=models.CharField(max_length=100)
    type_of_doctor=models.CharField(max_length=50)
    degree=models.CharField(max_length=300)
    experience=models.FloatField(default=0.0)
    review=models.FloatField(default=0.0)
    medical_registration=models.IntegerField(default=0)
    location=models.CharField(max_length=300)
    availability_dates_start=models.DateField(default='2023-01-01')
    availability_dates_end=models.DateField(default='2023-01-01')
    availability_times=models.TimeField(default='09:00:00')
    availability_times_end=models.TimeField(default='17:00:00')
    price=models.FloatField(default=100.0)
    address_clinic=models.CharField(max_length=400)
    
    def _str_(self):
        return f"""{self.doctor_name},
                    {self.type_of_doctor},
                    {self.degree},
                    {self.experience},
                    {self.review},
                    {self.medical_registration},
                    {self.location},
                    {self.availability_dates_start},
                    {self.availability_dates_end},
                    {self.availability_times},
                    {self.availability_times_end},
                    {self.price},
                    {self.address_clinic}"""
                    
class patient_details(models.Model):
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    age=models.FloatField(default=0.0)
    phone_number=models.IntegerField(default=0)
    locations=models.CharField(max_length=300)
    def _str_(self):
        return f"""{self.name},
                    {self.gender},
                    {self.age},
                    {self.phone_number},
                    {self.locations},"""

