from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import FileExtensionValidator
# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    licence = models.ImageField(upload_to='ehr/static', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])], null=True)
    phonenumber = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    emailid = models.EmailField()

    def __str__(self):
        return self.name

class Individual(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, null=True)
    age = models.IntegerField(default=0)
    DOB = models.DateField(default=timezone.now)
    address = models.TextField(null=True, blank=True)
    phonenumber = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    