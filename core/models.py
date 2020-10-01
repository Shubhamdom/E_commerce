from django.conf import settings
from django.db import models

# Create your models here.
class adminUserInfo(models.Model):
    name = models.CharField(max_length= 50)
    bs_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    




