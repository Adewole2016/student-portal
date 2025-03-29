

from django.db import models

class Non_Academic_Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    department = models.CharField(max_length=100)
    
    passport = models.ImageField(upload_to='non_academic_staff_passports/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

