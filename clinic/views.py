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
    



# Doctor view

class DoctorBaseView(views.TemplateView):
    template_name = "clinic/doctor/doctor_base.html"
    model = core_models.DoctorModel
    form_class = core_forms.DoctorForm

class DoctorDashboardView(views.TemplateView):
    template_name = "clinic/doctor/doctor_dashboard.html"
    model = core_models.DoctorModel

class DoctorPatientView(views.TemplateView):
    template_name = "clinic/doctor/doctor_patient.html"
    model = core_models.DoctorModel

class DoctorAppointmentView(views.TemplateView):
    template_name = "clinic/doctor/doctor_appointment.html"
    model = core_models.DoctorModel

class DoctorViewAppointmentView(views.TemplateView):
    template_name = "clinic/doctor/doctor_appointment.html"
    model = core_models.DoctorModel

class DoctorDeleteAppointmentView(views.DeleteView):
    template_name = "clinic/doctor/doctor_appointment.html"
    model = core_models.DoctorModel
    




# Patient view

class PatientListView(views.ListView):
    template_name = "clinic/patient/patient_list.html"
    model = core_models.PatientModel

class PatientCreateView(views.CreateView):
    template_name = "clinic/patient/patient_create.html"
    model = core_models.PatientModel
    form_class = core_forms.PatientForm

class PatientDetailView(views.DetailView):
    template_name = "clinic/patient/patient_detail.html"
    model = core_models.PatientModel

class PatientUpdateView(views.UpdateView):
    template_name = "clinic/patient/patient_update.html"
    model = core_models.PatientModel
    form_class = core_forms.PatientForm

class PatientDeleteView(views.DeleteView):
    template_name = "clinic/patient/patient_delete.html"
    model = core_models.PatientModel
