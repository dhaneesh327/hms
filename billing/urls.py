from django.urls import path
from billing import views as billing_views

app_name = "billing"
urlpatterns = [
    path("billing/<int:pk>/",billing_views.BillingView.as_view(),name="billing"),
]