from django.db import models
from django.conf import settings

from core import models as core_models
from django.contrib.auth.models import User

# Create your models here.

class DepartmentModel(core_models.TimeStampedModel):
    department_name=models.CharField(max_length=55)

    def __str__(self):
        return self.department_name

class DoctorModel(core_models.TimeStampedModel):
    name=models.CharField(max_length=30)
    profile_pic=models.ImageField(upload_to='doctor/image/', default='default/doc_photo.jpg')
    speciality=models.CharField(max_length=30)
    department=models.ForeignKey(DepartmentModel,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=15)
    year_of_experience=models.IntegerField()
    about=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
       

class PatientModel(core_models.TimeStampedModel):
    class GenderChoices(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"
        TRANSGEDER = "T", "Transgender"
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=3, choices=GenderChoices.choices)
    blood_group=models.CharField(max_length=3)
    address=models.CharField(max_length=100)
    patient_type=models.CharField(max_length=55)

    def __str__(self):
        return self.name
 
class AppointmentModel(core_models.TimeStampedModel):
    name=models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    email=models.EmailField()
    doctor=models.ForeignKey(DoctorModel,on_delete=models.CASCADE)
    appointment_date=models.DateTimeField()
    reason=models.CharField(max_length=255)
    status=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class MedicalHistoryModel(core_models.TimeStampedModel):
    patient = models.ForeignKey(PatientModel,on_delete=models.CASCADE)
    disease = models.CharField(max_length=255)
    treatment = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.patient

class PrescriptionModel(core_models.TimeStampedModel):
    patient=models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    appointment = models.ForeignKey(AppointmentModel, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    days = models.IntegerField()
    medical_history=models.ForeignKey(MedicalHistoryModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.patient

class DischargeModel(core_models.TimeStampedModel):
    patient = models.ForeignKey(PatientModel,on_delete=models.CASCADE)
    admit_date = models.DateField()
    release_date = models.DateField()
    symptoms = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.patient
