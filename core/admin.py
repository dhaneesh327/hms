from django.contrib import admin
from core import models

# Register your models here.

admin.site.register(models.LocationModel)
admin.site.register(models.AddressModel)
admin.site.register(models.HospitalModel)
admin.site.register(models.ContactModel)
