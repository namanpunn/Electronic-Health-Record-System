from django.db import models

# Create your models here.
class Doctor (models.Model):
    name = models.CharField(max_length=200)  
    designation = models.CharField(max_length=20)  
    phonenumber = models.CharField(max_length=10)  

    def __str__(Self):
        return Self.name

class Individual (models.Model):
    name = models.CharField(max_length=20)  
    Address = models.TextField(null=True, blank=True)  
    phonenumber = models.CharField(max_length=10)  

    def __str__(Self):
        return Self.name