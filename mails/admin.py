from django.contrib import admin
from mails import models as mails_models

# Register your models here.

admin.site.register(mails_models.MailModel)
