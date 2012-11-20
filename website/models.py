from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    upc_code = models.CharField(max_length=12, primary_key=True)
    product_name = models.TextField()
    product_brand = models.CharField(max_length=20)
    product_desc = models.TextField()
    only_online = models.BooleanField()
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_weight = models.DecimalField(max_digits=5, decimal_places=2)
    product_volume = models.DecimalField(max_digits=7, decimal_places=2)

class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_addr = models.CharField(max_length=120)
    store_items = models.ForeignKey('Product')
    store_employees = models.ForeignKey('Employee')
    store_items_sold = models.IntegerField()

class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_firstName = models.CharField(max_length=30)
    emp_lastName = models.CharField(max_length=30)
    emp_wage_hour = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(User, unique=True)

class StoreContains(models.Model):
    store = models.ForeignKey('Store')
    product = models.ForeignKey('Product')
    num_sold = models.IntegerField()
