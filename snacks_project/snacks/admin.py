from csv import list_dialects
from django.contrib import admin
from .models import Snack


@admin.register(Snack)
class AdminSnack(admin.ModelAdmin):
    list_display = [
        "name",
        "calories",
        "vegan",
        "gloten_free",
        "sugar_free",
        "lactose_free",
    ]
