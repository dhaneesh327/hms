from django.shortcuts import render
from django.views import generic as views
from billing import models as core_models
from billing import forms as core_forms

# Create your views here.

class BillingView(views.View):
    template_name = "billing/billing.html"
    model = core_models.BillingModel
    form_class = core_forms.BillingForm