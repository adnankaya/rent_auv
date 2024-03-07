from django.urls import path, include
from rest_framework import routers

from apps.renting import views as renting_views
from apps.uav import views as uav_views

app_name = "api"

router = routers.DefaultRouter(trailing_slash=True)
router.register("renting", renting_views.RentingViewset, basename="renting")
router.register("uav", uav_views.UavViewset, basename="uav")
router.register("categories", uav_views.CategoryViewset, basename="categories")

urlpatterns = [
    path("", include((router.urls, "routers"))),


]
