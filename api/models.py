from email.policy import default
from operator import mod
from random import choice
from tkinter import CASCADE
from django.db import models
from distutils.command.upload import upload
from django.contrib.auth.models import User
from django.forms import CharField, IntegerField


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


class Invoice(models.Model):

    INVOICE = 'invoice'
    CREDIT_NOTE = 'credit_note'

    CHOICES_TYPE = (
        (INVOICE, 'Invoice'),
        (CREDIT_NOTE, 'Credit note')
    )

    invoice_number = models.IntegerField(default=1)
    client_name = models.CharField(max_length=200)
    client_email = models.CharField(max_length=250)
    client_org_number  = models.CharField(max_length=250)
    client_adress = models.CharField(max_length=250)
    client_country = models.CharField(max_length=200)
    client_contact = models.CharField(max_length=200)
    invoice_type = models.CharField(max_length=250,  choices=CHOICES_TYPE, default=INVOICE)
    due_days = models.IntegerField(default=14)
    is_credit_for = models.ForeignKey('self',blank=True,null=True, on_delete=models.CASCADE)
    is_sent = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    gross_amount = models.DecimalField(max_digits=6, decimal_places=2)
    vat_amount = models.DecimalField(max_digits=6, decimal_places=2)
    net_amount = models.DecimalField(max_digits=6, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=6, decimal_places=2)
    client = models.ForeignKey(abakiriya, related_name='invoices', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='created_invoices', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return '%r' % self.client_name, self.client_country


class Item(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=130)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    net_amount = models.DecimalField(max_digits=6, decimal_places=2)
    vat_rate = models.IntegerField()
    discount = models,IntegerField()





  