from django import forms
from mails import models as mails_models

class MailForm(forms.ModelForm):
    class Meta:
        model = mails_models.MailModel
        fields = [
            "sender",
            "receiver",
            "subject",
            "message",
            "attachments",
        ]