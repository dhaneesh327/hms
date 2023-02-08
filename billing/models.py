from django.db import models
from django.conf import settings
from core import models as core_models
from clinic import models as clinic_models
# Create your models here.

class BillingModel(core_models.TimeStampedModel):
    patient = models.ForeignKey(clinic_models.PatientModel, on_delete=models.CASCADE)
    insurance_details=models.CharField(max_length=55)
    room_charge=models.PositiveIntegerField()
    medicine_cost=models.PositiveIntegerField()
    doctor_fee=models.PositiveIntegerField()
    other_charges=models.PositiveIntegerField()

    def __str__(self):
        return self.patient
