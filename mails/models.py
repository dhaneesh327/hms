from django.db import models
from django.conf import settings

from core import models as core_models
from django.contrib.auth.models import User

# Create your models here.

class MailModel(core_models.TimeStampedModel):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    subject = models.CharField(max_length=255)
    message = models.TextField()
    attachments = models.FileField(upload_to='attachments/')
