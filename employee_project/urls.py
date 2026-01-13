from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from employee_register.forms import CustomLoginForm

urlpatterns = [
    path("admin/", admin.site.urls),
    # login / logout
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="employee_register/login.html",
            authentication_form=CustomLoginForm,  # now it is defined
        ),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # employee app URLs
    path("employee/", include("employee_register.urls")),
]
