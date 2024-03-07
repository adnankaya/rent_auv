from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.core.pagination import BasePageNumberPagination
from .serializers import RentingSerializer, RentingListSerializer
from .models import Renting
from .filters import RentingFilter


class RentingViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = RentingSerializer
    filterset_class = RentingFilter
    pagination_class = BasePageNumberPagination

    def get_queryset(self):
        qs = Renting.objects.all()
        user = self.request.user
        if not user.is_superuser:
            qs = qs.filter(user=user)
        return qs.select_related("user", "uav").order_by("-created_date")

    def get_serializer_class(self):
        if self.action == "list":
            return RentingListSerializer
        return super().get_serializer_class()

    def perform_update(self, serializer):
        # return super().perform_update(serializer)
        instance = serializer.save(updated_by=self.request.user)

    def perform_destroy(self, instance):
        # Instead of actually deleting the object, set is_deleted to True
        instance.is_deleted = True
        instance.save()
