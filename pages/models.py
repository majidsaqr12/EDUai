# models.py
from django.db import models

class Offer(models.Model):
    CATEGORY_CHOICES = [
        ('Primary', 'Primary'),
        ('Middle School', 'Middle School'),
        ('High School', 'High School')
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    monthly_price = models.DecimalField(max_digits=10, decimal_places=2)
    quarterly_price = models.DecimalField(max_digits=10, decimal_places=2)
    annually_price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='TND')  # Added currency field

    def __str__(self):
        return self.category
