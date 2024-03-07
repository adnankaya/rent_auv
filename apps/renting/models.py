from django.db import models
from django.contrib.auth import get_user_model
from apps.core.models import BaseModel


User = get_user_model()


class Renting(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uav = models.ForeignKey("uav.Uav", on_delete=models.CASCADE)
    updated_by = models.ForeignKey(
        User,
        related_name="updated_rentings",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "t_renting"
