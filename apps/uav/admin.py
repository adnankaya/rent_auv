from django.contrib import admin

# Register your models here.
from .models import Uav, Category

admin.site.register(Category)
admin.site.register(Uav)