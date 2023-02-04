from django.shortcuts import redirect,render
from django.views import generic as views
from clinic import models as core_models
from clinic import forms as core_forms
# Create your views here.

# Appointment View

class AppointmentListView(views.ListView):
    template_name = "clinic/appointment/appointment_list.html"
    model = core_models.AppointmentModel

class AppointmentCreateView(views.CreateView):
    template_name = "clinic/appointment/appointment_create.html"
    model = core_models.AppointmentModel
    form_class = core_forms.AppointmentForm

class AppointmentDetailView(views.DetailView):
    template_name = "clinic/appointment/appointment_detail.html"
    model = core_models.AppointmentModel

class AppointmentUpdateView(views.UpdateView):
    template_name = "clinic/appointment/appointment_update.html"
    model = core_models.AppointmentModel
    form_class = core_forms.AppointmentForm

class AppointmentDeleteView(views.DeleteView):
    template_name = "clinic/appointment/appointment_delete.html"
    model = core_models.AppointmentModel
    

# Patient view

class PatientProfileView(views.View):
    template_name = "clinic/patient/patient_profile.html"
    model = core_models.PatientModel
    form_class = core_forms.PatientForm

# precription view

class AddPrescriptionView(views.View):
    template_name = "clinic/prescription/add_prescription.html"
    model = core_models.PrescriptionModel
    form_class = core_forms.PrescriptionForm

class ShowPrescriptionView(views.View):
    template_name = "clinic/prescription/show_prescription.html"
    model = core_models.PrescriptionModel
    form_class = core_forms.PrescriptionForm

class MedicalHistoryView(views.View):
    template_name = "clinic/prescription/medical_history.html"
    model = core_models.PrescriptionModel