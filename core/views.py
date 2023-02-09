from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views
from django.views.generic import FormView

from core import forms as core_forms
from core import models as core_models

# HomeView


class HomeView(views.TemplateView):
    template_name = "core/home.html"


class AboutView(views.TemplateView):
    template_name = "core/about.html"


# Sending feedback
class ContactView(views.FormView):
    template_name = "core/contact.html"
    form_class = core_forms.ContactForm
    success_url = reverse_lazy("core:contact")

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        subject = form.cleaned_data["subject"]
        message = form.cleaned_data["message"]
        phone_number = form.cleaned_data["phone_number"]

        # Save the feedback to the database
        contact = core_models.ContactModel.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            phone_number=phone_number,
        )

        # Send an auto-generated email to the user
        send_mail(
            "Thank you for your feedback",
            "Thank you for your feedback, we will get back to you soon",
            "no-reply@example.com",
            [email],
            # fail_silently=False,
        )

        return super().form_valid(form)
