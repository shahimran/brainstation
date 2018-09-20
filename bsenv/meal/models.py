from django.db import models
from django.utils import timezone
from decimal import Decimal


class Token(models.Model):
    empName = models.CharField(max_length=200)
    empId = models.DecimalField( max_digits=19, decimal_places=0)
    phone = models.DecimalField(max_digits=13, decimal_places=0)
    lunch = models.CharField(max_length=20)
    meal_date = models.DateField(auto_now=True)


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, blank=True)
    phone = models.DecimalField(max_digits=13, decimal_places=0)
    password = models.CharField(max_length=50)


class Data(models.Model):
    firstName = models.CharField(max_length=200, null=True)
    lastName = models.CharField(max_length=200, null=True)