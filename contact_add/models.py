from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class add_user(models.Model):
    add_by = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    Contact = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
   