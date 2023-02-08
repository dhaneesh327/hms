from django.contrib import admin
from core import models as core_models

# Register your models here.

admin.site.register(core_models.LocationModel)
admin.site.register(core_models.AddressModel)
admin.site.register(core_models.HospitalModel)
admin.site.register(core_models.ProfileModel)
admin.site.register(core_models.ContactModel)
