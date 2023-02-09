from django.urls import include, path

from accounts import views

app_name = "accounts"

urlpatterns = [
    # Profile
    path("profile/create/", views.ProfileDetailView.as_view(), name="profile_create"),
    path("profile/<int:pk>/", views.ProfileDetailView.as_view(), name="profile_detail"),
    path("profile/<int:pk>/update/", views.ProfileDetailView.as_view(), name="profile_update"),
    path("profile/<int:pk>/delete/", views.ProfileDetailView.as_view(), name="profile_delete"),
    # Authentication
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("", include("django.contrib.auth.urls")),
]
