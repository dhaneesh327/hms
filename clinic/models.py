from django.db import models
from django.conf import settings

from core import models as core_models
from django.contrib.auth.models import User

# Create your models here.

class HospitalModel(core_models.TimeStampedModel):
    name=models.CharField(max_length=55)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.ForeignKey(core_models.AddressModel, on_delete=models.CASCADE)    

class DepartmentModel(core_models.TimeStampedModel):
    hospital=models.ForeignKey(HospitalModel,on_delete=models.CASCADE)
    name=models.CharField(max_length=55)

class DoctorModel(core_models.TimeStampedModel):
    name=models.CharField(max_length=30)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='doctor/image/', default='default/doc_photo.jpg')
    speciality=models.CharField(max_length=30)
    department=models.ForeignKey(DepartmentModel,on_delete=models.CASCADE)
    mobile=models.IntegerField()
    year_of_experience=models.IntegerField()
    about=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
        
class PatientTypemodel(models.Model):
    patient_type=models.CharField(max_length=30)   

class PatientModel(core_models.TimeStampedModel):
    class GenderChoices(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"
        TRANSGEDER = "T", "Transgender"
    name=models.CharField(max_length=30)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    age=models.IntegerField()
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=3, choices=GenderChoices.choices)
    blood_group=models.CharField(max_length=3)
    address=models.ForeignKey(core_models.AddressModel,on_delete=models.CASCADE)
    patient_type=models.ForeignKey(PatientTypemodel,on_delete=models.CASCADE)
    admitDate=models.DateField(auto_now=True)
     
class StaffModel(core_models.TimeStampedModel):
    name=models.CharField(max_length=30)
    profile_pic=models.ImageField(upload_to='')
    speciality=models.CharField(max_length=30)
    department=models.ForeignKey(DepartmentModel,on_delete=models.CASCADE)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    year_of_experience=models.IntegerField()
    about=models.CharField(max_length=255)
 
class AppointmentModel(core_models.TimeStampedModel):
    doctor=models.ForeignKey(DoctorModel,on_delete=models.CASCADE)
    patient=models.ForeignKey(PatientModel,on_delete=models.CASCADE)
    appointment_date=models.DateTimeField()
    reason=models.CharField(max_length=255)
    fee=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=255)
    patient_type=models.ForeignKey(PatientTypemodel, on_delete=models.CASCADE)

class MedicalHistoryModel(core_models.TimeStampedModel):
    patient = models.ForeignKey(PatientModel,on_delete=models.CASCADE)
    disease = models.CharField(max_length=255)
    treatment = models.TextField()
    date = models.DateTimeField()

class PrescriptionModel(core_models.TimeStampedModel):
    appointment = models.ForeignKey(AppointmentModel, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    days = models.IntegerField()
    medical_history=models.ForeignKey(MedicalHistoryModel,on_delete=models.CASCADE)
