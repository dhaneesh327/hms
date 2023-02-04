from django.urls import path
from core import views as core_views

app_name = "core"
urlpatterns = [
    path("", core_views.HomeView.as_view(), name="home"),
    path("about/",core_views.AboutView.as_view(),name="about"),
    path("contact/",core_views.ContactView.as_view(),name="contact"),
# login
    path('login/',core_views.LoginView.as_view(), name='login'),
    path('signup/',core_views.SignupView.as_view(), name='signup'),
    path('logout/',core_views.LogoutView.as_view(), name='logout'),
]