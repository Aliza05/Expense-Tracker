from django.urls import path
from . import views

app_name = "tracker"


urlpatterns = [
    path("", views.homepage, name="homepage"),

    path("register", views.register_request, name="register"),

    path("login", views.login_request, name="login"),

    path("logout", views.logout_request, name="logout"),

    path("debit_form", views.debit_form, name="debit_form"),

    path("debit", views.debit, name="debit"),

    path("credit_form", views.credit_form, name="credit_form"),

    path("credit", views.credit, name="credit")
]
