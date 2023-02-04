from django.urls import path
from mails import views as mails_views

app_name = "mails"
urlpatterns = [
    path("list/",mails_views.MailListView.as_view(),name="mail_list"),
    path("<int:pk>/Create/",mails_views.MailCreateView.as_view(),name="mail_create"),  
    path("<int:pk>/update/",mails_views.MailUpdateView.as_view(),name="mail_update"),
    path("<int:pk>/delete/",mails_views.MailDeleteView.as_view(),name="mail_delete"),
]