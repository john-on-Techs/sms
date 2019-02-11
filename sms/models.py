from django.db import models
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.urls import reverse
import datetime

# from django.core.exceptions import
# Create your models here.
from django import forms


class Product(models.Model):
    PRODUCT_CHOICES = (
        ('K', 'Kerosene'),
        ('P', 'Petrol'),
        ('S', 'Super'),
    )

    name = models.CharField(max_length=1, choices=PRODUCT_CHOICES, default='K', unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_name_display()


class Station(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class StationProductPrice(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.station) + "-" + str(self.product)

    class Meta:
        unique_together = ('product', 'station')


class UserStation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    station = models.OneToOneField(Station, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + " " + str(self.station)

    class Meta:
        unique_together = ('user', 'station')


class SaleRecord(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number_of_litres = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_litre = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, editable=False)
    amount_collected = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, editable=False)
    entry_at = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('station', 'product', 'entry_at')
        ordering = ['-entry_at']

    def __str__(self):
        return str(self.product)

    def get_absolute_url(self):
        return reverse('sms:detail', args=[str(self.pk)])

    def save(self, *args, **kwargs):
        self.price_per_litre = StationProductPrice.objects.get(station=self.station, product=self.product).price
        self.amount_collected = self.price_per_litre * self.number_of_litres
        super(SaleRecord, self).save(*args, **kwargs)
