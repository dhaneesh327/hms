from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import generic as views
from django.contrib.auth import views as auth_views

from core import forms as core_forms
from core import models as core_models

from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

from django.core.mail import send_mail
from django.views.generic import FormView
# Create your views here.

class LoginView(views.View):
    form_class=AuthenticationForm
    template_name="core/registration/login.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form":form})

    def post(self, request ,*args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("core:home")
        return render(request, self.template_name, {"form":form})

class SignupView(views.View):
    form_class = UserCreationForm
    template_name = "core/registration/signup.html"
    success_url = reverse_lazy("core:home")

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url)
        return render(request, self.template_name, {"form": form})

class LogoutView(views.View):
    success_url = reverse_lazy("core:home")

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(self.success_url)


# profile view 

class ProfileCreateView(views.CreateView):
    template_name = "core/profile/profile_create.html"
    model = core_models.ProfileModel
    form_class = core_forms.ProfileForm

class ProfileDetailView(LoginRequiredMixin, views.DetailView):
    template_name = "core/profile/profile_detail.html"
    model = core_models.ProfileModel
    context_object_name = "profile"


class ProfileUpdateView(views.UpdateView):
    template_name = "core/profile/profle_update.html"
    model = core_models.ProfileModel
    form_class = core_forms.ProfileForm


class ProfileDeleteView(views.DeleteView):
    template_name = "core/profile/profile_delete.html"
    model = core_models.ProfileModel

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