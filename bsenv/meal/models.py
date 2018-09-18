from django.db import models
from django.utils import timezone

# Create your models here.
class Token(models.Model):
    empName = models.CharField(max_length=200)
    empId = models.DecimalField( max_digits=19, decimal_places=10)
    meal_date = models.DateTimeField(auto_now=True)
