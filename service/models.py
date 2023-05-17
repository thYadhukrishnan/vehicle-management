from django.db import models

class Service(models.Model):
    vehicle_number=models.CharField(max_length=50)
    vehicle_type=models.CharField(max_length=50)
    vehicle_model=models.CharField(max_length=50)
    vehicle_desc=models.CharField(max_length=50)

# Create your models here.
