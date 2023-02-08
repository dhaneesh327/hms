from django import forms
from billing import models as billing_models

class BillingForm(forms.ModelForm):
    class Meta:
        model = billing_models.BillingModel
        fields = [
            "patient",
            "insurance_details",
            "room_charge",
            "medicine_cost",
            "doctor_fee",
            "other_charges",
        ]
           