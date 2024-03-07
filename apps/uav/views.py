from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import status, response


from apps.core.pagination import BasePageNumberPagination
from apps.uav.filters import UavFilter
from apps.uav.models import Uav, Category
from apps.uav.serializers import (
    UavSerializer,
    UavCreateSerializer,
    UavUpdateSerializer,
    CategorySerializer,
)
from apps.renting.services import RentingService
from apps.renting.serializers import UavRentSerializer


class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class UavViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UavSerializer
    pagination_class = BasePageNumberPagination
    filterset_class = UavFilter

    def get_queryset(self):
        qs = Uav.objects.select_related("created_by", "category").order_by(
            "model", "created_date"
        )
        return qs

    def get_serializer_class(self):
        if self.action == "create":
            return UavCreateSerializer
        if self.action == "update":
            return UavUpdateSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        return super().perform_create(serializer)

    def perform_destroy(self, instance):
        # soft deletion
        instance.is_deleted = True
        instance.save()

    @action(detail=True, methods=["post"])
    def rent(self, request, pk):
        try:
            serializer = UavRentSerializer(data=request.data)
            if serializer.is_valid():
                obj = RentingService().create_renting_object(
                    request.user, serializer.validated_data
                )
                serializer.instance = obj
                return response.Response(
                    serializer.data, status=status.HTTP_201_CREATED
                )
            return response.Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return response.Response(str(e), status=status.HTTP_400_BAD_REQUEST)


def index(request):
    context = {"title": _("UAVs page")}
    return render(request, "uav/index.html", context)


@login_required
def new_uav(request):
    context = {"title": _("New UAV page")}
    return render(request, "uav/new-uav.html", context)


@login_required
def renting_uav(request, uav_id):
    context = {"title": _("Rent UAV page")}
    context.update({"uav_id": uav_id})
    return render(request, "uav/renting.html", context)


@login_required
def update_uav(request, uav_id):
    context = {"title": _("Update UAV page")}
    context.update({"uav_id": uav_id})
    return render(request, "uav/update.html", context)
