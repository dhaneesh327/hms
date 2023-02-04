from django import forms
from billing import models as billing_models

class BillingForm(forms.ModelForm):
    class Meta:
        model = billing_models.BillingModel
        fields = [
            "room_charge",
            "medicine_cost",
            "doctor_fee",
            "other_charge",
            "total",
            "date",
        ]

class InsuranceForm(forms.ModelForm):
    class Meta:
        model = billing_models.InsuranceModel
        fields = [
            "patient",
            "company_name",
            "policy_number",
            "expiry_date",
            "coverage",
        ]

class DischargeForm(forms.ModelForm):
    class Meta:
        model = billing_models.DischargeModel
        fields = [
            "patient",
            "date",
            "condition",
        ]      