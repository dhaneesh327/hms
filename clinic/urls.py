from django.urls import path
from clinic import views as clinic_views

app_name = "clinic"
urlpatterns = [
    # appointment urls
    path("appointment/list/",clinic_views.AppointmentListView.as_view(),name="appointment_list"),
    path("appointment/Create/",clinic_views.AppointmentCreateView.as_view(),name="appointment_create"),  
    path("appointment/detail/",clinic_views.AppointmentDetailView.as_view(),name="appointment_detail"),
    path("appointment/<int:pk>/update/",clinic_views.AppointmentUpdateView.as_view(),name="appointment_update"),
    path("appointment/<int:pk>/delete/",clinic_views.AppointmentDeleteView.as_view(),name="appointment_delete"),
    # Patient urls
    path("patient/<int:pk>/profile/",clinic_views.PatientProfileView.as_view(),name="patient_profile"),
    # prescription urls
    path("prescription/<int:pk>/medicalhistory/",clinic_views.MedicalHistoryView.as_view(),name="medical_history"),
    path("prescription/<int:pk>/add_prescription/",clinic_views.AddPrescriptionView.as_view(),name="add_prescription"),
    path("prescription/<int:pk>/show_prescription/",clinic_views.ShowPrescriptionView.as_view(),name="show_prescription"),
]