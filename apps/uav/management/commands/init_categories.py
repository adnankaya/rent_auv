# -*- coding: utf-8 -*-
import json
from django.core.management.base import BaseCommand
from django.db import transaction


class Command(BaseCommand):
    help = "Generate Category Data"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS("\n{} Process started...{}\n").format(
                self.help, __name__
            )
        )
        try:
            with transaction.atomic():
                self.stdout.write(self.style.SUCCESS("\Category creation\n"))
                from apps.uav.models import Category

                # Create new data
                c_jet, cj = Category.objects.get_or_create(name="JET")
                c_hale, ch = Category.objects.get_or_create(name="HALE")
                c_tactical, ct = Category.objects.get_or_create(name="TACTICAL")

        except Exception as e:
            raise e

        self.stdout.write(self.style.SUCCESS("Process finished"))
