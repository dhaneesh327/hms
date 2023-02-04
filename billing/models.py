from django.db import models
from django.conf import settings
from core import models as core_models
from clinic import models as clinic_models
# Create your models here.

class BillingModel(core_models.TimeStampedModel):
    room_charge=models.PositiveIntegerField()
    medicine_cost=models.PositiveIntegerField()
    doctor_fee=models.PositiveIntegerField()
    other_charge=models.PositiveIntegerField()
    total=models.PositiveIntegerField()
    date=models.DateTimeField()

class InsuranceModel(core_models.TimeStampedModel):
    patient = models.ForeignKey(clinic_models.PatientModel, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    policy_number = models.CharField(max_length=255)
    expiry_date = models.DateTimeField()
    coverage = models.CharField(max_length=255)

class DischargeModel(core_models.TimeStampedModel):
    patient = models.ForeignKey(clinic_models.PatientModel,on_delete=models.CASCADE)
    date = models.DateField()
    condition = models.CharField(max_length=255)
