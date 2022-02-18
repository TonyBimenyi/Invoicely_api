from django.db import models
from distutils.command.upload import upload
from django.contrib.auth.models import User


# Create your models here.


class Provider(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    birthdate = models.DateField()
    phone = models.BigIntegerField()

    #  def __str__(self):
    #     return f'{self.name} - {self.phone}'

class abakiriya(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    org_number = models.CharField(max_length=200, blank=True, null=True)
    address1 = models.CharField(max_length=200, blank=True, null=True)
    address2 =models.CharField(max_length=200, blank=True, null=True)
    zipcode = models.CharField(max_length=200, blank=True, null=True)
    place = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    contact_person = models.CharField(max_length=200, blank=True, null=True)
    contact_reference = models.CharField(max_length=200, blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return '%s' % self.name, self.email

    class Team(models.Model):
        name = models.CharField(max_length=200)
        org_number = models.CharField(max_length=200)
        first_invoice_number = models.IntegerField(default=1)
        created_by = models.ForeignKey(User, related_name='teams', on_delete=models.CASCADE)

        


  