from django.urls import path, include

from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="index"),
    path("pricing/", views.pricing, name="pricing"),
    path("contact/", views.contact, name="contact"),
    path("about-us/", views.aboutus, name="aboutus"),
    path("faq/", views.faq, name="faq"),
    path("privacy/", views.privacy, name="privacy"),
    path("terms/", views.terms, name="terms"),
    path("dashboard/", views.dashboard, name="dashboard"),
    
    
]
