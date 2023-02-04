from django import forms
from django.contrib import auth
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model
from core import models as core_models

USER = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm):
    class Meta:
        model = USER
        fields = ["username","email"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = core_models.ProfileModel
        fields = [
            "user",
            "phone_number",
            "address",
        ]

# contact form
class ContactForm(forms.ModelForm):
   class Meta:
        fields = ["name", "email", "phone_number","subject", "message"]
        model = core_models.ContactModel