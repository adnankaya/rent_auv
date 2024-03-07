# -*- coding: utf-8 -*-
import json
from django.core.management.base import BaseCommand
from django.db import transaction
from django.contrib.auth import get_user_model
User = get_user_model()

images = [
    {
        "1": "static/assets/uavs/kizilelma/1.png",
        "2": "static/assets/uavs/kizilelma/2.png",
        "3": "static/assets/uavs/kizilelma/3.png",
    },
    {
        "1": "static/assets/uavs/akinci/1.png",
        "2": "static/assets/uavs/akinci/2.png",
        "3": "static/assets/uavs/akinci/3.png",
    },
    {
        "1": "static/assets/uavs/tb2/1.png",
        "2": "static/assets/uavs/tb2/2.png",
        "3": "static/assets/uavs/tb2/3.png",
    },
    {
        "1": "static/assets/uavs/tb3/1.png",
        "2": "static/assets/uavs/tb3/2.png",
        "3": "static/assets/uavs/tb3/3.png",
    },
]


class Command(BaseCommand):
    help = "Generate Demo Data"

    

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS("\n{} Process started...{}\n").format(
                self.help, __name__
            )
        )
        try:
            with transaction.atomic():
                self.stdout.write(self.style.SUCCESS("\Demo UAV creation\n"))
                from apps.uav.models import Category, Uav
                # Delete existings
                Category.objects.all().delete()
                Uav.objects.all().delete()
                # Create new data
                admin = User.objects.get(username="admin")
                c_jet,cj = Category.objects.get_or_cerate(name="JET")
                c_hale,ch = Category.objects.get_or_cerate(name="HALE")
                c_tactical,ct = Category.objects.get_or_cerate(name="TACTICAL")
                Uav.objects.create(created_by=admin,category=c_jet,brand="bayraktar", model="kizilelma", weight=8500, image_urls=images[0])
                Uav.objects.create(created_by=admin,category=c_hale,brand="bayraktar", model="akinci", weight=6000, image_urls=images[1])
                Uav.objects.create(created_by=admin,category=c_tactical,brand="bayraktar", model="tb2", weight=750.5, image_urls=images[2])
                Uav.objects.create(created_by=admin,category=c_tactical,brand="bayraktar", model="tb3", weight=1450.3, image_urls=images[3])
            

        except Exception as e:
            raise e

        self.stdout.write(self.style.SUCCESS("Process finished"))
