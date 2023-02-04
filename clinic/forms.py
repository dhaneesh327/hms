from django import forms
from clinic import models as clinic_models

class HospitalForm(forms.ModelForm):
    class Meta:
        model = clinic_models.HospitalModel
        fields = [
            "name",
            "phone_number",
            "email",
            "address",
        ]

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = clinic_models.DepartmentModel
        fields = [
            "hospital",
            "name",
        ]

class DoctorForm(forms.ModelForm):
    class Meta:
        model = clinic_models.DoctorModel
        fields = [
            "department",
            "name",
            "speciality",
            "user",
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
            "patient_type",
        ]        

class StaffForm(forms.ModelForm):
    class Meta:
        model = clinic_models.StaffModel
        fields = [
            "department",
            "name",
            "speciality",
            "user",
            "year_of_experience",
            "about",
        ]

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = clinic_models.AppointmentModel
        fields = [
            "doctor",
            "patient",
            "appointment_date",
            "reason",
            "fee",
            "status",
            "patient_type",
        ]


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = clinic_models.PrescriptionModel
        fields = [
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
