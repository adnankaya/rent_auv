# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Generate users Data"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS("\n{} Process started...{}\n").format(
                self.help, __name__
            )
        )
        try:
            User = get_user_model()
            user, _ = User.objects.get_or_create(
                username="admin",
                first_name="adnan",
                last_name="kaya",
                email="admin@example.com",
            )
            user.is_active = True
            user.is_staff = True
            user.is_superuser = True
            user.set_password("password")
            user.save()

        except Exception as e:
            raise e

        self.stdout.write(self.style.SUCCESS("Process finished"))
