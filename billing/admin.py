from django.contrib import admin
from billing import models as billing_models

# Register your models here.

admin.site.register(billing_models.BillingModel)
