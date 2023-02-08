from django.urls import path
from clinic import views as clinic_views

app_name = "clinic"
urlpatterns = [
    # appointment urls
    path("appointment/list/",clinic_views.AppointmentListView.as_view(),name="appointment_list"),
    path("appointment/Create/",clinic_views.AppointmentCreateView.as_view(),name="appointment_create"),  
    path("appointment/<int:pk>/detail/",clinic_views.AppointmentDetailView.as_view(),name="appointment_detail"),
    path("appointment/<int:pk>/update/",clinic_views.AppointmentUpdateView.as_view(),name="appointment_update"),
    path("appointment/<int:pk>/delete/",clinic_views.AppointmentDeleteView.as_view(),name="appointment_delete"),
    # doctor urls
    path("doctor/doctor_base/",clinic_views.DoctorBaseView.as_view(),name="doctor_base"),
    path("doctor/doctor_dashboard/",clinic_views.DoctorDashboardView.as_view(),name="doctor_dashboard"),
    path("doctor/doctor_patient/",clinic_views.DoctorPatientView.as_view(),name="doctor_patient"),
    path("doctor/doctor_appointment/",clinic_views.DoctorAppointmentView.as_view(),name="doctor_appointment"),
    path("doctor/doctor_view_appointment/",clinic_views.DoctorViewAppointmentView.as_view(),name="doctor_view_appointment"),
    path("doctor/doctor_appointment/",clinic_views.DoctorDeleteAppointmentView.as_view(),name="doctor_delete_appointment"),
    # Patient urls
    path("patient/list/",clinic_views.PatientListView.as_view(),name="patient_list"),
    path("patient/Create/",clinic_views.PatientCreateView.as_view(),name="patient_create"),  
    path("patient/<int:pk>/detail/",clinic_views.PatientDetailView.as_view(),name="patient_detail"),
    path("patient/<int:pk>/update/",clinic_views.PatientUpdateView.as_view(),name="patient_update"),
    path("patient/<int:pk>/delete/",clinic_views.PatientDeleteView.as_view(),name="patient_delete"),
]