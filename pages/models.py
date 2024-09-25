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

class Testimonial(models.Model):
    student_name = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/', default='videos/default.mp4')  # Default video
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name


class FAQCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class FAQ(models.Model):
    category = models.ForeignKey(FAQCategory, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
    
class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    complaint_type = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.full_name