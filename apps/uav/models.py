from django.db import models
from django.contrib.auth import get_user_model

from apps.core.models import BaseModel

from django.core.validators import MaxValueValidator, MinValueValidator


User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        db_table = "t_category"

    def __str__(self) -> str:
        return self.name


class Uav(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    brand = models.CharField(max_length=120, db_index=True)
    model = models.CharField(max_length=120, unique=True)
    weight = models.FloatField(
        validators=[MinValueValidator(0.1), MaxValueValidator(32000.0)],
    )
    image_urls = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = "t_uav"

    def __str__(self) -> str:
        return f"{self.brand} - {self.model}"
