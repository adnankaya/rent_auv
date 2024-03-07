from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("me/", views.me_profile, name="me"),
    
]
