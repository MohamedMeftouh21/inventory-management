from django.db import models
from Product.models import * 
from django.contrib import admin
from dal import autocomplete
# Create your models here.

    


class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


 
class Invoice(models.Model):
    items = models.ManyToManyField(Item)
    date = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

  
    def __str__(self):
        return f"Invoice #{self.id}"

   