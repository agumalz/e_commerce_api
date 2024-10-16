from django.db import models

# Create your models here.

class ProvinceModel(models.Model):
    province_id = models.CharField(max_length=255)
    province = models.CharField(max_length=255)