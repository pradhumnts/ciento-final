from django.db import models
from ambassador.models import Membership

# Create your models here.
class Affiliate(models.Model):
    affiliateName = models.CharField(max_length=40)
    number = models.IntegerField()
    profile = models.URLField()
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    instagram = models.CharField(max_length=400)
    membership = models.ManyToManyField(Membership, blank=True, related_name="affiliates")

class SubAffiliate(models.Model):
    member_id = models.ForeignKey('member.Member', on_delete=models.CASCADE)
    affiliate_id = models.ForeignKey(Affiliate, on_delete=models.CASCADE)
    add_affiliates = models.BooleanField()
    change_offers = models.BooleanField()
    see_reports = models.BooleanField()
    scan_members = models.BooleanField()
    get_notifications = models.BooleanField()

class Offer(models.Model):
    one_day = "one-day"
    three_day = "three-day"
    one_week = "one_week" 
    one_month = "one_month"
    forever = "forever"
    offer_limt = [
        (one_day, 'one-day'),
        (three_day, 'three-day'),
        (one_week, 'one_week'),
        (one_month, 'one_month'),
        (forever, 'forever'),
    ]
    
    affiliate_id = models.ForeignKey(Affiliate, on_delete=models.CASCADE)
    offer_discription = models.CharField(max_length=200)
    date_valid_till = models.DateField()
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    offer_limit = models.CharField(max_length=40, choices=offer_limt)
    photo_offer = models.URLField(blank=True, null=True)
