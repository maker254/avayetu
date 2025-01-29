from django.contrib import admin
from production.models import Customer,Vehicle

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    pass
    