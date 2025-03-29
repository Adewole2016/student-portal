

from django.db import models

class Lecturer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    department = models.CharField(max_length=100)
    courses_taught = models.TextField(blank=True, help_text="List courses separated by commas")
    passport = models.ImageField(upload_to='lecturer_passports/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

