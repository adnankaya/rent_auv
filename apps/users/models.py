
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from apps.core.models import BaseModel, BaseUuidModel


class User(AbstractUser):

    class Meta:
        db_table = "t_user"

    def __str__(self) -> str:
        return self.email or self.username

    def get_full_name(self) -> str:
        fullname = super().get_full_name()
        if not fullname:
            return self.username
        return fullname