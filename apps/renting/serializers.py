from rest_framework import serializers

from apps.renting.models import Renting
from apps.uav.serializers import UavSerializer

class RentingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Renting
        fields = "__all__"

class RentingListSerializer(RentingSerializer):
    user_name = serializers.ReadOnlyField(source="user.get_full_name")
    uav = UavSerializer()

class UavRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Renting
        fields = ("uav",)