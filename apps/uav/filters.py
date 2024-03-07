from django_filters import rest_framework as filters

from .models import Uav


class UavFilter(filters.FilterSet):
    created_date = filters.DateFromToRangeFilter()
    brand = filters.CharFilter(lookup_expr='icontains')
    model = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Uav
        fields = [
            "created_date",
            "is_deleted",
            "model",
            "brand",
        ]

    