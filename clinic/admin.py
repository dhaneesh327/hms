from django.contrib import admin
from clinic import models as clinic_models

# Register your models here.

admin.site.register(clinic_models.DepartmentModel)
admin.site.register(clinic_models.DoctorModel)
admin.site.register(clinic_models.PatientModel)
admin.site.register(clinic_models.AppointmentModel)
admin.site.register(clinic_models.PrescriptionModel)
admin.site.register(clinic_models.MedicalHistoryModel)
