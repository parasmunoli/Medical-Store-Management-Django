from django.db import models
from django.conf import settings

DEFAULT_AUTO_FIELD = getattr(settings, 'DEFAULT_AUTO_FIELD', 'django.db.models.AutoField')
# Create your models here.
class Dealer(models.Model):
    id = models.AutoField(primary_key=True)
    dname = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phn_no = models.BigIntegerField(unique=True)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.email


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    e_id = models.IntegerField(unique=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    sal = models.CharField(max_length=20)
    phn_no = models.BigIntegerField(unique=True)

    def __str__(self):
        return self.email


class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phn_no = models.BigIntegerField()
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.email


class Medicine(models.Model):
    id = models.BigAutoField(primary_key=True)
    m_id = models.IntegerField(unique=True)
    mname = models.CharField(max_length=30)
    dname = models.CharField(max_length=30)
    desc = models.CharField(max_length=100)
    price = models.CharField(max_length=30)
    stock = models.IntegerField()

    def __str__(self):
        return self.mname


class Purchase(models.Model):
    id = models.BigAutoField(primary_key=True)
    pname = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    phn_no = models.BigIntegerField()
    price = models.BigIntegerField()
    qty = models.BigIntegerField()
    total = models.BigIntegerField()

    def __str__(self):
        return self.pname
