from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
Genders = (("Male", "Male"),("Female", "Female"),("Other", "Other"))

class Registeration(models.Model):
    Name = models.CharField(max_length=69)
    Email = models.EmailField()
    Mobile = models.CharField(max_length=13)
    Password = models.CharField(max_length=69)
    Gender = models.CharField(
        max_length = 10,
        choices = Genders,
        default = 'Male'
    )