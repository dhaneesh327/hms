from django.shortcuts import render
from mails import models as mails_models
from mails import forms as mails_forms
from django.views import generic as views
# Create your views here.

# Mail view 

class MailListView(views.ListView):
    template_name = "mails/mail_list.html"
    model = mails_models.MailModel

class MailCreateView(views.CreateView):
    template_name = "mails/mail_create.html"
    model = mails_models.MailModel
    form_class = mails_forms.MailForm

class MailUpdateView(views.UpdateView):
    template_name = "mails/mail_update.html"
    model = mails_models.MailModel
    form_class = mails_forms.MailForm

class MailDeleteView(views.DeleteView):
    template_name = "mails/mail_delete.html"
    model = mails_models.MailModel