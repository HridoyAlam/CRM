import email
from enum import auto
from secrets import choice
from sre_constants import CATEGORY
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models

from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, null= True)
    phone = models.CharField(max_length=11, null= True)
    email = models.CharField(max_length=200, null= True)
    date_created = models.DateTimeField(auto_now_add = True, null= True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )
    name = models.CharField(max_length=200, null = True)
    price = models.FloatField(null = True)
    category = models.CharField(max_length = 200, null = True,choices = CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ("Out for delivary", "Out dor dor delivary"),
        ("Delivered", "delivered"),
        
    )

    date_created = models.DateTimeField(auto_now_add= True, null = True)
    status = models.CharField(max_length=200, null = True, choices= STATUS)