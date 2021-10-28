from django.db import models

Male = "Male"
Female = "Female"
Other = "Other"

Gender = [
    (Male, 'Male'),
    (Female, 'Female'),
    (Other, 'Other'),
]

# Create your models here.
class Ambassador(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    profile = models.URLField(blank=True, null=True)
    number = models.IntegerField()
    gender = models.CharField(max_length=40, choices=Gender)
    dob = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=40)
    address = models.CharField(max_length=100)

class SecondAmbassador(models.Model):
    ambassador_id = models.ForeignKey(Ambassador, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    profile = models.URLField(blank=True, null=True)
    number = models.IntegerField()
    gender = models.CharField(max_length=40, choices=Gender)
    dob = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    add_ambassador = models.BooleanField()
    change_offers = models.BooleanField()
    see_reports = models.BooleanField()
    invite_members = models.BooleanField()
    get_notifications = models.BooleanField()

class Membership(models.Model):
    ambassador_id = models.ForeignKey(Ambassador, on_delete=models.CASCADE)
    valid_till = models.DateTimeField()
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    require_photo_id = models.BooleanField()
