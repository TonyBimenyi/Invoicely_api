from django.db import models


# Create your models here.


class Provider(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    birthdate = models.DateField()
    phone = models.BigIntegerField()

  