from django.conf import settings
from django.db import models

from core.models import AddressModel, TimeStampedModel

USER = settings.AUTH_USER_MODEL


class ProfileModel(TimeStampedModel):
    class GenderChoices(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"
        TRANSGENDER = "T", "Transgender"

    user = models.OneToOneField(USER, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, default="")
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=3, choices=GenderChoices.choices)
    phone_number = models.CharField(max_length=16)
    address = models.ForeignKey(AddressModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
