from django.db import models

# Create your models here.
Male = "Male"
Female = "Female"
Other = "Other"

Gender = [
    (Male, 'Male'),
    (Female, 'Female'),
    (Other, 'Other'),
]

class SecondAdmin(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    number = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    approve_ambassador_affiliate = models.BooleanField()
    see_reports = models.BooleanField()
    get_notifications = models.BooleanField()

# class membership(models.Model):