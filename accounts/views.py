from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from accounts import forms, models


class ProfileBaseView(PermissionRequiredMixin, LoginRequiredMixin):
    pass


class ProfileCreateView(ProfileBaseView, views.CreateView):
    template_name = "core/profile/profile_create.html"
    model = models.ProfileModel
    form_class = forms.ProfileForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileDetailView(ProfileBaseView, views.DetailView):
    template_name = "core/profile/profile_detail.html"
    model = models.ProfileModel
    context_object_name = "profile"


class ProfileUpdateView(ProfileBaseView, views.UpdateView):
    template_name = "core/profile/profle_update.html"
    model = models.ProfileModel
    form_class = forms.ProfileForm


class ProfileDeleteView(ProfileBaseView, views.DeleteView):
    template_name = "core/profile/profile_delete.html"
    model = models.ProfileModel


# Authentication Views


class LoginView(LoginView):
    redirect_authenticated_user = True

    def form_valid(self, form):
        return super().form_valid(form)


class SignupView(views.CreateView):
    template_name = "registration/signup.html"
    model = get_user_model()
    form_class = forms.SignupForm
    success_url = reverse_lazy("accounts:profile_detail")
