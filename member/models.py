from django.db import models
from ambassador.models import Membership

# Create your models here.
Male = "Male"
Female = "Female"
Other = "Other"

Gender = [
    (Male, 'Male'),
    (Female, 'Female'),
    (Other, 'Other'),
]

class Member(models.Model):
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    nickName = models.CharField(max_length=60)
    profile = models.URLField(blank=True, null=True)
    number = models.IntegerField()
    gender = models.CharField(max_length=40, choices=Gender)
    dob = models.DateField()
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    memberships = models.ManyToManyField(Membership, blank=True, related_name="members_membership")
    affiliates = models.ManyToManyField('affiliate.Affiliate', blank=True, related_name="members_affiliate")
    photo_id = models.URLField(blank=True, null=True)
