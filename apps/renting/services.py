import logging
from django.db import transaction
from django.contrib.auth import get_user_model

from apps.core.services import CoreService
from apps.renting.models import Renting

User = get_user_model()

logger = logging.getLogger(__name__)


class RentingService(CoreService):

    def create_renting_object(self, user, validated_data: dict) -> Renting:
        try:
            renting = Renting.objects.create(user=user, **validated_data)
            return renting
        except Exception as e:
            logger.exception(e)
            raise e
