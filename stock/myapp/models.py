from django.db import models
from django.forms import forms
from django.urls import reverse


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    @property
    def total_price(self):
        return self.unit_price * self.quantity

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])
