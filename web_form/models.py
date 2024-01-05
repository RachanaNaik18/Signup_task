from django.db import models

# Create your models here.
class user_form(models.Model):
    name = models.CharField(max_length=150, null=True)
    email= models.EmailField(max_length=150, null=True)
    city= models.CharField(max_length=100, default=False)
    gender=models.CharField(max_length=100, default=True)
    SSC = models.BooleanField(default=False)
    HSC = models.BooleanField(default=False)
    graduate = models.BooleanField(default=False)
