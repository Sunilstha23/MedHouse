from django.db import models
from django.core import validators

# Create your models here.
class Lab(models.Model):
    full_name = models.CharField(max_length=120)
    lab_name = models.CharField(max_length=200)
    hospital_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    gender = models.CharField(max_length=10, default="none")
    contact_number = models.IntegerField()
    pan_number = models.CharField(max_length=10)
    vat_number = models.CharField(max_length=10)
    password = models.CharField(max_length=25)
    timestamp = models.DateTimeField(auto_now_add=True)
    services = models.CharField(validators.validate_comma_separated_integer_list, max_length=200)
    location = models.CharField(max_length=50)
    branches = models.IntegerField()
    branLocation = models.CharField(validators.validate_comma_separated_integer_list, max_length=200)
    
class LabImage(models.Model):
    PROFILE = 'profile'
    PAN = 'pan'
    VAT = 'vat'
    CITIZENSHIP = 'citizenship'
    LICENSE = 'license'

    IMAGE_TYPES = [
        (PROFILE, 'Profile Picture'),
        (PAN, 'PAN Card'),
        (VAT, 'VAT'),
        (CITIZENSHIP, 'Citizenship Card'),
        (LICENSE, 'License'),
    ]

    lab_id = models.ForeignKey(Lab, on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    image_path = models.CharField(max_length=256)
    img_type = models.CharField(max_length=12, choices=IMAGE_TYPES, default=LICENSE)
    timestamp = models.DateTimeField(auto_now_add=True)
