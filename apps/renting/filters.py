from django_filters import rest_framework as filters

from .models import Renting


class RentingFilter(filters.FilterSet):
    created_date = filters.DateFromToRangeFilter()
    model = filters.CharFilter(method="filter_by_uav_model")
    brand = filters.CharFilter(method="filter_by_uav_brand")

    class Meta:
        model = Renting
        fields = [
            "created_date",
            "is_deleted",
        ]

    def filter_by_uav_model(self, queryset, name, value):
        if value is not None:
            return queryset.filter(uav__model__iexact=value)

    def filter_by_uav_brand(self, queryset, name, value):
        if value is not None:
            return queryset.filter(uav__brand__iexact=value)
