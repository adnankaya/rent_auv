from django.urls import path, include
from . import views

app_name = "uav"


urlpatterns = [
    path("<uav_id>/update", views.update_uav, name="update"),
    path("<uav_id>/rent", views.renting_uav, name="rent"),
    path("new/", views.new_uav, name="new"),
    path("", views.index, name="index"),

]
