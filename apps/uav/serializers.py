from rest_framework import serializers

from apps.uav.models import Uav, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class BaseUavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uav
        fields = (
            "id",
            "brand",
            "model",
            "weight",
            "image_urls",
            "category",
            "created_date",
            "updated_date",
            "is_deleted",
        )


class UavSerializer(BaseUavSerializer):
    category_name = serializers.SerializerMethodField("get_category_name")

    class Meta(BaseUavSerializer.Meta):
        fields = BaseUavSerializer.Meta.fields + ("category_name", "created_by")

    def get_category_name(self, obj: Uav):
        return obj.category.name


class UavCreateSerializer(BaseUavSerializer):

    class Meta(BaseUavSerializer.Meta):
        fields = BaseUavSerializer.Meta.fields


class UavUpdateSerializer(BaseUavSerializer):

    pass
