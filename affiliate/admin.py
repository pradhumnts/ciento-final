from django.contrib import admin
from .models import Affiliate, SubAffiliate, Offer

# Register your models here.
admin.site.register(Affiliate)
admin.site.register(SubAffiliate)
admin.site.register(Offer)