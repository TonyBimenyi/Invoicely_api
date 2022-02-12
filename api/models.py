from django.db import models
from distutils.command.upload import upload


# Create your models here.


class Provider(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    birthdate = models.DateField()
    phone = models.BigIntegerField()

    #  def __str__(self):
    #     return f'{self.name} - {self.phone}'

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    birthdate = models.DateField()
    email = models.EmailField()
    phone = models.BigIntegerField()


  