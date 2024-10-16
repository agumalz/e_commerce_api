from django.db import models
from province.models import ProvinceModel

# Create your models here.
class CityModel(models.Model):
    city_id = models.CharField(max_length=255)
    city_name = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)  
    