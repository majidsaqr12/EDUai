from django.db import models
from django.utils import timezone

class Mathematics(models.Model):
    file = models.FileField(upload_to='pdfs/mathematics/')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Mathematics"

class English(models.Model):
    file = models.FileField(upload_to='pdfs/english/')
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return "English"

class Chemistry(models.Model):
    file = models.FileField(upload_to='pdfs/chemistry/')
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return "Chemistry"

class Geography(models.Model):
    file = models.FileField(upload_to='pdfs/geography/')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Geography"

class Science(models.Model):
    file = models.FileField(upload_to='pdfs/science/')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Science"

class History(models.Model):
    file = models.FileField(upload_to='pdfs/history/')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "History"

class Biology(models.Model):
    file = models.FileField(upload_to='pdfs/biology/')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Biology"

class Physics(models.Model):
    file = models.FileField(upload_to='pdfs/physics/')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Physics"

class Arabic(models.Model):
    file = models.FileField(upload_to='pdfs/arabic/')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Arabic"

class French(models.Model):
    file = models.FileField(upload_to='pdfs/french/')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "French"
