from django.contrib import admin
from .models import Ambassador, SecondAmbassador, Membership

# Register your models here.
admin.site.register(Ambassador)
admin.site.register(SecondAmbassador)
admin.site.register(Membership)