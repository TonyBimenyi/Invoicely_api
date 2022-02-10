from django.db import models


# Create your models here.


class Providers(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    birthdate = models.DateField
    phone = models.BigIntegerField 

  