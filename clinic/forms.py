from django import forms
from clinic import models as clinic_models

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = clinic_models.DepartmentModel
        fields = [
            "department_name",
        ]

class DoctorForm(forms.ModelForm):
    class Meta:
        model = clinic_models.DoctorModel
        fields = [
            "profile_pic",
            "name",
            "department",
            "speciality",
            "phone_number",
            "year_of_experience",
            "about",
        ]

class PatientForm(forms.ModelForm):
    class Meta:
        model = clinic_models.PatientModel
        fields = [
            "name",
            "age",
            "date_of_birth",
            "gender",
            "address",
            "blood_group",
            "patient_type",
        ]        


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = clinic_models.AppointmentModel
        fields = [
            "name",
            "phone_number",
            "email",
            "doctor",
            "appointment_date",
            "reason",
            "status",
        ]

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = clinic_models.PrescriptionModel
        fields = [
            "patient",
            "appointment",
            "medicine_name",
            "dosage",
            "days",
        ]

class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = clinic_models.MedicalHistoryModel
        fields = [
            "patient",
            "disease",
            "treatment",
            "date",
        ]

class DischargeForm(forms.ModelForm):
    class Meta:
        model = clinic_models.DischargeModel
        fields = [
            "patient",
            "admit_date",
            "release_date",
            "symptoms",
            "phone_number",
            "address",
        ] 
